/**
 * RESTful API Service
 * 使用 Express.js 构建的 Web API 服务
 *
 * 展示异步编程、中间件模式、错误处理
 *
 * Author: Demo Code
 * Created: 2026-04-08
 */

const express = require('express');
const helmet = require('helmet');
const compression = require('compression');

// WHY: 使用类来组织相关功能，而不是分散的函数
// 这样更容易维护和测试
class ApiService {
  constructor(config = {}) {
    // IMPORTANT: 配置应该验证后再使用
    this.config = {
      port: config.port || 3000,
      env: config.env || 'development',
      ...config
    };

    this.app = express();
    this.setupMiddleware();
    this.setupRoutes();
    this.setupErrorHandling();
  }

  /**
   * 配置中间件
   *
   * NOTE: 中间件的顺序非常重要
   * 1. 安全设置 (helmet)
   * 2. 压缩 (compression)
   * 3. 请求解析 (express.json)
   * 4. 自定义中间件
   */
  setupMiddleware() {
    // 安全头部
    this.app.use(helmet());

    // 压缩响应
    this.app.use(compression());

    // 解析 JSON 请求体
    this.app.use(express.json());

    // 请求日志
    // HACK: 简单的日志实现，生产环境应该用 Winston 或 Bunyan
    this.app.use((req, res, next) => {
      console.log(`${req.method} ${req.path}`);
      next();
    });

    // TODO: 添加认证中间件
    // this.app.use(authenticate);
  }

  /**
   * 设置路由
   *
   * WHY: 将路由定义分离，使代码更清晰
   * 可以很容易地添加新的路由或修改现有路由
   */
  setupRoutes() {
    const router = express.Router();

    // 健康检查
    router.get('/health', (req, res) => {
      res.json({
        status: 'healthy',
        timestamp: new Date().toISOString(),
        uptime: process.uptime()
      });
    });

    // CRUD 操作
    router
      .route('/items')
      .get(this.getItems.bind(this))     // 获取列表
      .post(this.createItem.bind(this)); // 创建新项

    router
      .route('/items/:id')
      .get(this.getItem.bind(this))      // 获取单个
      .put(this.updateItem.bind(this))   // 更新
      .delete(this.deleteItem.bind(this)); // 删除

    // 挂载路由
    this.app.use('/api/v1', router);
  }

  /**
   * 错误处理中间件
   *
   * IMPORTANT: 错误处理中间件必须有 4 个参数
   * Express 通过参数数量识别错误处理中间件
   */
  setupErrorHandling() {
    // 404 处理
    this.app.use((req, res) => {
      res.status(404).json({
        error: 'Not Found',
        path: req.path
      });
    });

    // 全局错误处理
    // NOTE: 这个中间件必须在所有路由之后
    this.app.use((err, req, res, next) => {
      console.error('Error:', err);

      // HACK: 简单的错误分类，实际应该更精细
      const statusCode = err.statusCode || 500;
      const message = this.config.env === 'production'
        ? 'Internal Server Error'
        : err.message;

      res.status(statusCode).json({
        error: message,
        ...(this.config.env !== 'production' && { stack: err.stack })
      });
    });
  }

  // ============ 路由处理器 ============

  /**
   * 获取所有项目
   *
   * WHY: 使用 async/await 而不是 Promise 链
   * 代码更易读，错误处理更简单
   */
  async getItems(req, res, next) {
    try {
      // TODO: 从数据库获取实际数据
      const items = [
        { id: 1, name: 'Item 1' },
        { id: 2, name: 'Item 2' }
      ];

      res.json({
        success: true,
        data: items,
        count: items.length
      });
    } catch (error) {
      next(error);
    }
  }

  /**
   * 创建新项目
   */
  async createItem(req, res, next) {
    try {
      const { name, description } = req.body;

      // IMPORTANT: 输入验证应该在业务逻辑之前
      if (!name || name.trim().length === 0) {
        return res.status(400).json({
          error: 'Name is required'
        });
      }

      // TODO: 保存到数据库
      const newItem = {
        id: Date.now(),
        name: name.trim(),
        description: description || '',
        createdAt: new Date().toISOString()
      };

      res.status(201).json({
        success: true,
        data: newItem
      });
    } catch (error) {
      next(error);
    }
  }

  /**
   * 获取单个项目
   */
  async getItem(req, res, next) {
    try {
      const { id } = req.params;

      // TODO: 从数据库获取
      const item = { id, name: `Item ${id}` };

      if (!item) {
        return res.status(404).json({
          error: 'Item not found'
        });
      }

      res.json({
        success: true,
        data: item
      });
    } catch (error) {
      next(error);
    }
  }

  /**
   * 更新项目
   */
  async updateItem(req, res, next) {
    try {
      const { id } = req.params;
      const updates = req.body;

      // TODO: 更新数据库记录
      const updatedItem = {
        id,
        ...updates,
        updatedAt: new Date().toISOString()
      };

      res.json({
        success: true,
        data: updatedItem
      });
    } catch (error) {
      next(error);
    }
  }

  /**
   * 删除项目
   */
  async deleteItem(req, res, next) {
    try {
      const { id } = req.params;

      // TODO: 从数据库删除
      // IMPORTANT: 软删除通常比硬删除更好
      // 可以保留数据用于审计或恢复

      res.status(204).send();
    } catch (error) {
      next(error);
    }
  }

  /**
   * 启动服务器
   */
  start() {
    return new Promise((resolve) => {
      this.server = this.app.listen(this.config.port, () => {
        console.log(`API server running on port ${this.config.port}`);
        resolve();
      });
    });
  }

  /**
   * 停止服务器
   *
   * WHY: 优雅关闭很重要
   * 可以等待正在处理的请求完成
   */
  async stop() {
    return new Promise((resolve) => {
      if (this.server) {
        this.server.close(() => {
          console.log('API server stopped');
          resolve();
        });
      } else {
        resolve();
      }
    });
  }
}

// NOTE: 导出类，支持不同的使用方式
module.exports = ApiService;

// 如果直接运行此文件，启动服务器
if (require.main === module) {
  const service = new ApiService({ port: 3000 });
  service.start();

  // 优雅关闭
  process.on('SIGTERM', () => {
    console.log('SIGTERM received, shutting down...');
    service.stop().then(() => process.exit(0));
  });
}
