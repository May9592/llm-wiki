// Web Server in Go
// 使用 Gin 框架构建的 RESTful API 服务器
//
// 展示：
// - 结构体和方法
// - 接口实现
// - 并发处理
// - 中间件模式
//
// Author: Demo Code
// Created: 2026-04-08

package main

import (
	"encoding/json"
	"fmt"
	"log"
	"net/http"
	"strconv"
	"sync"
	"time"

	"github.com/gin-gonic/gin"
)

// ============ 数据结构 ============

// User 用户结构体
// WHY: 使用 JSON 标签控制序列化
// 这是 Go 中处理 API 的标准方式
type User struct {
	ID        string    `json:"id"`
	Name      string    `json:"name" binding:"required"`
	Email     string    `json:"email" binding:"required,email"`
	CreatedAt time.Time `json:"created_at"`
	UpdatedAt time.Time `json:"updated_at,omitempty"`
}

// UserRepository 用户存储接口
//
// IMPORTANT: 使用接口而不是具体实现
// 这样可以轻松替换存储后端（内存、数据库、缓存等）
type UserRepository interface {
	Create(user *User) error
FindByID(id string) (*User, error)
	Update(id string, user *User) error
	Delete(id string) error
	List() ([]User, error)
}

// InMemoryUserRepository 内存存储实现
//
// NOTE: 使用读写锁保证并发安全
// Go 的 map 不是并发安全的，需要加锁
type InMemoryUserRepository struct {
	mu    sync.RWMutex
	users map[string]*User
}

// NewInMemoryUserRepository 创建新的存储实例
func NewInMemoryUserRepository() *InMemoryUserRepository {
	return &InMemoryUserRepository{
		users: make(map[string]*User),
	}
}

// Create 创建用户
func (r *InMemoryUserRepository) Create(user *User) error {
	r.mu.Lock()
	defer r.mu.Unlock()

	user.ID = generateID()
	user.CreatedAt = time.Now()
	r.users[user.ID] = user

	return nil
}

// FindByID 根据 ID 查找用户
func (r *InMemoryUserRepository) FindByID(id string) (*User, error) {
	r.mu.RLock()
	defer r.mu.RUnlock()

	user, exists := r.users[id]
	if !exists {
		return nil, fmt.Errorf("user not found")
	}

	return user, nil
}

// Update 更新用户
func (r *InMemoryUserRepository) Update(id string, user *User) error {
	r.mu.Lock()
	defer r.mu.Unlock()

	if _, exists := r.users[id]; !exists {
		return fmt.Errorf("user not found")
	}

	user.ID = id
	user.UpdatedAt = time.Now()
	r.users[id] = user

	return nil
}

// Delete 删除用户
func (r *InMemoryUserRepository) Delete(id string) error {
	r.mu.Lock()
	defer r.mu.Unlock()

	if _, exists := r.users[id]; !exists {
		return fmt.Errorf("user not found")
	}

	delete(r.users, id)
	return nil
}

// List 列出所有用户
func (r *InMemoryUserRepository) List() ([]User, error) {
	r.mu.RLock()
	defer r.mu.RUnlock()

	users := make([]User, 0, len(r.users))
	for _, user := range r.users {
		users = append(users, *user)
	}

	return users, nil
}

// ============ 服务层 ============

// UserService 用户服务
//
// WHY: 分离业务逻辑和数据访问
// 遵循单一职责原则
type UserService struct {
	repo UserRepository
}

// NewUserService 创建服务实例
func NewUserService(repo UserRepository) *UserService {
	return &UserService{repo: repo}
}

// CreateUser 创建新用户
func (s *UserService) CreateUser(name, email string) (*User, error) {
	user := &User{
		Name:  name,
		Email: email,
	}

	if err := s.repo.Create(user); err != nil {
		return nil, err
	}

	return user, nil
}

// GetUser 获取用户
func (s *UserService) GetUser(id string) (*User, error) {
	return s.repo.FindByID(id)
}

// UpdateUser 更新用户
func (s *UserService) UpdateUser(id string, name, email string) (*User, error) {
	user, err := s.repo.FindByID(id)
	if err != nil {
		return nil, err
	}

	user.Name = name
	user.Email = email

	if err := s.repo.Update(id, user); err != nil {
		return nil, err
	}

	return user, nil
}

// DeleteUser 删除用户
func (s *UserService) DeleteUser(id string) error {
	return s.repo.Delete(id)
}

// ListUsers 列出所有用户
func (s *UserService) ListUsers() ([]User, error) {
	return s.repo.List()
}

// ============ HTTP 处理器 ============

// UserHandler 用户 HTTP 处理器
type UserHandler struct {
	service *UserService
}

// NewUserHandler 创建处理器
func NewUserHandler(service *UserService) *UserHandler {
	return &UserHandler{service: service}
}

// CreateUserRequest 创建请求
type CreateUserRequest struct {
	Name  string `json:"name" binding:"required"`
	Email string `json:"email" binding:"required,email"`
}

// UpdateUserRequest 更新请求
type UpdateUserRequest struct {
	Name  string `json:"name" binding:"required"`
	Email string `json:"email" binding:"required,email"`
}

// ApiResponse 响应结构
type ApiResponse struct {
	Success bool        `json:"success"`
	Data    interface{} `json:"data,omitempty"`
	Error   string      `json:"error,omitempty"`
}

// CreateUser 处理创建用户请求
func (h *UserHandler) CreateUser(c *gin.Context) {
	var req CreateUserRequest
	if err := c.ShouldBindJSON(&req); err != nil {
		c.JSON(http.StatusBadRequest, ApiResponse{
			Success: false,
			Error:   err.Error(),
		})
		return
	}

	user, err := h.service.CreateUser(req.Name, req.Email)
	if err != nil {
		c.JSON(http.StatusInternalServerError, ApiResponse{
			Success: false,
			Error:   err.Error(),
		})
		return
	}

	c.JSON(http.StatusCreated, ApiResponse{
		Success: true,
		Data:    user,
	})
}

// GetUser 获取单个用户
func (h *UserHandler) GetUser(c *gin.Context) {
	id := c.Param("id")

	user, err := h.service.GetUser(id)
	if err != nil {
		c.JSON(http.StatusNotFound, ApiResponse{
			Success: false,
			Error:   "user not found",
		})
		return
	}

	c.JSON(http.StatusOK, ApiResponse{
		Success: true,
		Data:    user,
	})
}

// ListUsers 列出所有用户
func (h *UserHandler) ListUsers(c *gin.Context) {
	users, err := h.service.ListUsers()
	if err != nil {
		c.JSON(http.StatusInternalServerError, ApiResponse{
			Success: false,
			Error:   err.Error(),
		})
		return
	}

	c.JSON(http.StatusOK, ApiResponse{
		Success: true,
		Data:    users,
	})
}

// UpdateUser 更新用户
func (h *UserHandler) UpdateUser(c *gin.Context) {
	id := c.Param("id")

	var req UpdateUserRequest
	if err := c.ShouldBindJSON(&req); err != nil {
		c.JSON(http.StatusBadRequest, ApiResponse{
			Success: false,
			Error:   err.Error(),
		})
		return
	}

	user, err := h.service.UpdateUser(id, req.Name, req.Email)
	if err != nil {
		c.JSON(http.StatusInternalServerError, ApiResponse{
			Success: false,
			Error:   err.Error(),
		})
		return
	}

	c.JSON(http.StatusOK, ApiResponse{
		Success: true,
		Data:    user,
	})
}

// DeleteUser 删除用户
func (h *UserHandler) DeleteUser(c *gin.Context) {
	id := c.Param("id")

	if err := h.service.DeleteUser(id); err != nil {
		c.JSON(http.StatusNotFound, ApiResponse{
			Success: false,
			Error:   "user not found",
		})
		return
	}

	c.Status(http.StatusNoContent)
}

// ============ 中间件 ============

// LoggerMiddleware 日志中间件
func LoggerMiddleware() gin.HandlerFunc {
	return func(c *gin.Context) {
		start := time.Now()

		// 处理请求
		c.Next()

		// 记录日志
		latency := time.Since(start)
		status := c.Writer.Status()
		method := c.Request.Method
		path := c.Request.URL.Path

		log.Printf("[%s] %s %s - Status: %d - Latency: %v",
			time.Now().Format(time.RFC3339),
			method, path, status, latency)
	}
}

// CORSMiddleware CORS 中间件
func CORSMiddleware() gin.HandlerFunc {
	return func(c *gin.Context) {
		c.Writer.Header().Set("Access-Control-Allow-Origin", "*")
		c.Writer.Header().Set("Access-Control-Allow-Methods", "GET, POST, PUT, DELETE, OPTIONS")
		c.Writer.Header().Set("Access-Control-Allow-Headers", "Content-Type, Authorization")

		if c.Request.Method == "OPTIONS" {
			c.AbortWithStatus(http.StatusNoContent)
			return
		}

		c.Next()
	}
}

// ============ 辅助函数 ============

// generateID 生成唯一 ID
//
// HACK: 简单实现，生产环境应该用 UUID 或雪花算法
func generateID() string {
	return fmt.Sprintf("user_%d", time.Now().UnixNano())
}

// ============ 主函数 ============

func main() {
	// NOTE: 开发环境使用 Debug 模式
	gin.SetMode(gin.DebugMode)

	// 创建路由
	router := gin.New()

	// 全局中间件
	router.Use(LoggerMiddleware())
	router.Use(CORSMiddleware())
	router.Use(gin.Recovery())

	// 创建依赖
	repo := NewInMemoryUserRepository()
	service := NewUserService(repo)
	handler := NewUserHandler(service)

	// 健康检查
	router.GET("/health", func(c *gin.Context) {
		c.JSON(http.StatusOK, gin.H{
			"status":    "healthy",
			"timestamp": time.Now().Format(time.RFC3339),
		})
	})

	// API 路由
	api := router.Group("/api/v1")
	{
		users := api.Group("/users")
		{
			users.GET("", handler.ListUsers)       // 列出所有用户
			users.POST("", handler.CreateUser)     // 创建用户
			users.GET("/:id", handler.GetUser)     // 获取单个用户
			users.PUT("/:id", handler.UpdateUser)  // 更新用户
			users.DELETE("/:id", handler.DeleteUser) // 删除用户
		}
	}

	// 启动服务器
	// IMPORTANT: 生产环境应该从配置读取端口
	port := 8080
	log.Printf("Starting server on port %d...", port)
	if err := router.Run(":" + strconv.Itoa(port)); err != nil {
		log.Fatal("Failed to start server:", err)
	}
}

/*
WHY: Go 语言的优势
-------------------
1. 高性能：编译型语言，接近 C 的性能
2. 并发：goroutine 和 channel 使并发编程简单
3. 类型安全：编译时检查，减少运行时错误
4. 标准库：丰富的标准库，减少外部依赖
5. 部署简单：单个二进制文件，无需运行时

TODO: 添加更多功能
-------------------
- 数据库持久化 (使用 GORM)
- JWT 认证
- 速率限制
- 指标收集 (Prometheus)
- 优雅关闭
*/
