/**
 * Type Definitions and Interfaces
 * TypeScript 类型系统示例
 *
 * 展示：
 * - 接口定义
 * - 泛型
 * - 联合类型
 * - 类型守卫
 * - 装饰器模式
 *
 * Author: Demo Code
 * Created: 2026-04-08
 */

// ============ 基础类型定义 ============

/**
 * 用户状态枚举
 *
 * WHY: 使用枚举而不是字符串字面量
 * 提供类型安全和更好的 IDE 支持
 */
enum UserStatus {
  ACTIVE = 'active',
  INACTIVE = 'inactive',
  SUSPENDED = 'suspended',
  PENDING = 'pending'
}

/**
 * 用户角色类型
 *
 * NOTE: 使用模板字面量类型创建严格的格式
 */
type RoleName = `role:${string}`;

/**
 * 用户接口
 *
 * IMPORTANT: 接口定义了对象的结构契约
 * TypeScript 会在编译时检查这些契约
 */
interface User {
  readonly id: string;              // 只读属性
  name: string;
  email: string;
  status: UserStatus;
  roles: RoleName[];
  metadata?: Record<string, any>;   // 可选属性
  createdAt: Date;
  updatedAt?: Date;
}

/**
 * 用户创建输入
 *
 * WHY: 分离创建和更新类型
 * 避免在创建时提供 id 和时间戳
 */
interface CreateUserInput {
  name: string;
  email: string;
  roles?: RoleName[];
}

/**
 * 用户更新输入
 *
 * NOTE: 所有属性都是可选的
 * 使用 Partial 工具类型自动实现
 */
type UpdateUserInput = Partial<CreateUserInput> & {
  status?: UserStatus;
};

// ============ 泛型定义 ============

/**
 * API 响应接口
 *
 * 使用泛型支持不同的数据类型
 * 类似于 Rust 的 Result 或 Go 的响应包装
 */
interface ApiResponse<T> {
  success: boolean;
  data?: T;
  error?: {
    code: string;
    message: string;
  };
  meta?: {
    timestamp: string;
    requestId: string;
  };
}

/**
 * 分页响应
 *
 * WHY: 组合泛型创建复杂类型
 */
interface PaginatedResponse<T> extends ApiResponse<T[]> {
  pagination: {
    page: number;
    pageSize: number;
    total: number;
    hasMore: boolean;
  };
}

/**
 * 结果类型
 *
 * 模拟 Rust 的 Result<T, E>
 * 用于表示可能失败的操作
 */
type Result<T, E = Error> =
  | { success: true; data: T }
  | { success: false; error: E };

// ============ 类型守卫 ============

/**
 * 检查是否为有效的用户对象
 *
 * WHY: 类型守卫帮助 TypeScript 在运行时识别类型
 * 在处理 JSON 数据或 API 响应时特别有用
 */
function isUser(obj: unknown): obj is User {
  return (
    typeof obj === 'object' &&
    obj !== null &&
    'id' in obj &&
    'name' in obj &&
    'email' in obj &&
    'status' in obj
  );
}

/**
 * 检查结果是否成功
 */
function isSuccess<T>(result: Result<T>): result is { success: true; data: T } {
  return result.success;
}

// ============ 高级类型 ============

/**
 * 事件类型
 *
 * 使用联合类型定义不同的事件
 */
type Event =
  | { type: 'click'; x: number; y: number }
  | { type: 'keydown'; key: string; code: string }
  | { type: 'scroll'; scrollTop: number };

/**
 * 事件处理器映射
 *
 * WHY: 使用映射类型创建类型安全的处理器
 */
type EventHandlerMap = {
  [K in Event['type']]: (event: Extract<Event, { type: K }>) => void;
};

// ============ 类定义 ============

/**
 * 抽象基础实体类
 *
 * IMPORTANT: 抽象类不能被实例化
 * 强制子类实现特定方法
 */
abstract class Entity {
  protected constructor(
    public readonly id: string,
    public readonly createdAt: Date = new Date()
  ) {}

  abstract validate(): boolean;
  abstract toJSON(): object;
}

/**
 * 用户类
 *
 * 继承自 Entity，实现特定行为
 */
class UserEntity extends Entity implements User {
  // HACK: 使用私有属性存储，通过 getter 访问
  #name: string;
  #email: string;
  #status: UserStatus;
  #roles: RoleName[];
  #metadata: Record<string, any>;
  #updatedAt?: Date;

  constructor(input: CreateUserInput & { id: string }) {
    super(input.id);
    this.#name = input.name;
    this.#email = input.email;
    this.#status = UserStatus.PENDING;
    this.#roles = input.roles || [];
    this.#metadata = {};
  }

  // Getters and Setters
  get name(): string {
    return this.#name;
  }

  set name(value: string) {
    // IMPORTANT: 在 setter 中添加验证逻辑
    if (value.trim().length === 0) {
      throw new Error('Name cannot be empty');
    }
    this.#name = value;
    this.#updatedAt = new Date();
  }

  get email(): string {
    return this.#email;
  }

  set email(value: string) {
    // TODO: 添加邮箱格式验证
    this.#email = value;
    this.#updatedAt = new Date();
  }

  get status(): UserStatus {
    return this.#status;
  }

  set status(value: UserStatus) {
    this.#status = value;
    this.#updatedAt = new Date();
  }

  get roles(): RoleName[] {
    return [...this.#roles]; // 返回副本
  }

  get metadata(): Record<string, any> {
    return { ...this.#metadata };
  }

  get updatedAt(): Date | undefined {
    return this.#updatedAt;
  }

  // Methods
  addRole(role: RoleName): void {
    // WHY: 检查角色是否已存在
    if (!this.#roles.includes(role)) {
      this.#roles.push(role);
      this.#updatedAt = new Date();
    }
  }

  removeRole(role: RoleName): void {
    this.#roles = this.#roles.filter(r => r !== role);
    this.#updatedAt = new Date();
  }

  update(input: UpdateUserInput): void {
    if (input.name) this.name = input.name;
    if (input.email) this.email = input.email;
    if (input.status) this.status = input.status;
  }

  validate(): boolean {
    return (
      this.#name.trim().length > 0 &&
      this.#email.includes('@') &&
      Object.values(UserStatus).includes(this.#status)
    );
  }

  toJSON(): User {
    return {
      id: this.id,
      name: this.#name,
      email: this.#email,
      status: this.#status,
      roles: this.#roles,
      metadata: this.#metadata,
      createdAt: this.createdAt,
      updatedAt: this.#updatedAt
    };
  }
}

// ============ 服务类 ============

/**
 * 用户服务类
 *
 * TODO: 添加缓存、批处理、事件发布等功能
 */
class UserService {
  // NOTE: 使用私有字段存储依赖
  #users: Map<string, UserEntity>;

  constructor() {
    this.#users = new Map();
  }

  /**
   * 创建用户
   */
  async create(input: CreateUserInput): Promise<Result<UserEntity>> {
    try {
      const id = this.generateId();
      const user = new UserEntity({ id, ...input });

      if (!user.validate()) {
        return {
          success: false,
          error: new Error('Invalid user data')
        };
      }

      this.#users.set(id, user);
      return { success: true, data: user };
    } catch (error) {
      return {
        success: false,
        error: error as Error
      };
    }
  }

  /**
   * 获取用户
   */
  async findById(id: string): Promise<Result<UserEntity>> {
    const user = this.#users.get(id);

    if (!user) {
      return {
        success: false,
        error: new Error('User not found')
      };
    }

    return { success: true, data: user };
  }

  /**
   * 更新用户
   */
  async update(id: string, input: UpdateUserInput): Promise<Result<UserEntity>> {
    const result = await this.findById(id);

    if (!isSuccess(result)) {
      return result;
    }

    result.data.update(input);
    return { success: true, data: result.data };
  }

  /**
   * 列出所有用户
   */
  async list(): Promise<UserEntity[]> {
    return Array.from(this.#users.values());
  }

  /**
   * 生成唯一 ID
   *
   * HACK: 简单实现，生产环境应该用 UUID 或雪花算法
   */
  private generateId(): string {
    return `user_${Date.now()}_${Math.random().toString(36).substr(2, 9)}`;
  }
}

// ============ 导出 ============

export type {
  User,
  CreateUserInput,
  UpdateUserInput,
  ApiResponse,
  PaginatedResponse,
  Result,
  Event,
  EventHandlerMap
};

export { UserStatus, UserEntity, UserService, isUser, isSuccess };
