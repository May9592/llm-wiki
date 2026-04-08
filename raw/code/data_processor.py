"""
Data Processing Pipeline
多阶段数据处理流水线，展示数据转换和验证模式

Author: Demo Code
Created: 2026-04-08
"""

import logging
from typing import List, Dict, Any, Optional
from dataclasses import dataclass
from datetime import datetime
import json

# WHY: 使用 dataclass 而不是普通类，为了减少样板代码
# Python 3.7+ 的 dataclass 自动生成 __init__、__repr__ 等方法
@dataclass
class DataRecord:
    """数据记录实体"""
    id: str
    content: str
    timestamp: datetime
    metadata: Dict[str, Any]
    is_valid: bool = True

    # NOTE: 这个方法会在序列化时被调用，确保数据一致性
    def to_dict(self) -> Dict[str, Any]:
        return {
            'id': self.id,
            'content': self.content,
            'timestamp': self.timestamp.isoformat(),
            'metadata': self.metadata,
            'is_valid': self.is_valid
        }


class DataValidator:
    """数据验证器 - 负责检查数据质量"""

    def __init__(self, rules: Optional[Dict[str, Any]] = None):
        # IMPORTANT: 规则应该在初始化时就确定，避免运行时修改
        self.rules = rules or self._default_rules()
        self.validation_count = 0

    def _default_rules(self) -> Dict[str, Any]:
        """默认验证规则"""
        return {
            'min_content_length': 10,
            'max_content_length': 10000,
            'required_fields': ['id', 'content']
        }

    # TODO: 添加更多验证规则，如格式检查、敏感词过滤等
    def validate(self, record: DataRecord) -> bool:
        """
        验证数据记录是否符合规则

        WHY: 分离验证逻辑，遵循单一职责原则
        每个类只负责一个核心功能
        """
        self.validation_count += 1

        # 检查必填字段
        if not record.id or not record.content:
            return False

        # 检查内容长度
        content_len = len(record.content)
        if content_len < self.rules['min_content_length']:
            return False
        if content_len > self.rules['max_content_length']:
            return False

        return True


class DataTransformer:
    """数据转换器 - 负责数据格式转换"""

    def __init__(self):
        self.transformations = []

    # IMPORTANT: 转换链的顺序很重要，先清洗后标准化
    def add_transformation(self, func):
        """添加转换函数到转换链"""
        self.transformations.append(func)
        return self

    def transform(self, record: DataRecord) -> DataRecord:
        """
        应用所有转换函数

        NOTE: 这种链式调用模式使转换流程清晰可读
        类似于 JavaScript 的 Promise 链或管道模式
        """
        result = record
        for transform_func in self.transformations:
            result = transform_func(result)
        return result

    # HACK: 这里用简单的字符串操作做演示
    # 生产环境应该使用更复杂的 NLP 处理
    @staticmethod
    def clean_text(record: DataRecord) -> DataRecord:
        """清洗文本内容"""
        content = record.content.strip()
        # 移除多余的空白
        content = ' '.join(content.split())
        record.content = content
        return record

    @staticmethod
    def normalize_case(record: DataRecord) -> DataRecord:
        """标准化大小写"""
        # IMPORTANT: 只标准化 content，保持 id 原样
        record.content = record.content.lower()
        return record


class DataEnricher:
    """数据增强器 - 添加额外的元数据和上下文"""

    def __init__(self, enrichment_source: Optional[Dict] = None):
        self.source = enrichment_source or {}

    # WHY: 数据增强是数据流中的一个独立阶段
    # 这样可以灵活地添加或删除增强逻辑
    def enrich(self, record: DataRecord) -> DataRecord:
        """为记录添加额外信息"""
        # TODO: 实现实际的数据增强逻辑
        # 例如：地理位置、分类标签、情感分析等

        enriched_metadata = {
            **record.metadata,
            'enriched_at': datetime.now().isoformat(),
            'enrichment_version': '1.0'
        }

        record.metadata = enriched_metadata
        return record


class DataPipeline:
    """
    数据处理流水线 - 协调整个处理流程

    这是核心协调器，类似于 knowledge_compiler.py 中的 KnowledgeCompiler
    """

    def __init__(self):
        # IMPORTANT: 组件的初始化顺序很重要
        # Validator → Transformer → Enricher
        self.validator = DataValidator()
        self.transformer = DataTransformer()
        self.enricher = DataEnricher()

        # NOTE: 配置转换链
        self.transformer.add_transformation(DataTransformer.clean_text)
        self.transformer.add_transformation(DataTransformer.normalize_case)

        self.stats = {
            'processed': 0,
            'valid': 0,
            'invalid': 0,
            'errors': 0
        }

    # WHY: 这个方法是流水线的入口点
    # 提供简单的接口给外部调用者
    def process(self, raw_data: List[Dict]) -> List[DataRecord]:
        """
        处理原始数据

        Args:
            raw_data: 原始数据字典列表

        Returns:
            处理后的 DataRecord 对象列表
        """
        results = []

        for data in raw_data:
            try:
                # 阶段1: 创建记录
                record = self._create_record(data)

                # 阶段2: 验证
                if not self.validator.validate(record):
                    self.stats['invalid'] += 1
                    continue

                # 阶段3: 转换
                record = self.transformer.transform(record)

                # 阶段4: 增强
                record = self.enricher.enrich(record)

                # 阶段5: 标记为有效
                record.is_valid = True

                results.append(record)
                self.stats['valid'] += 1

            except Exception as e:
                # HACK: 简单的错误处理，应该记录到日志
                self.stats['errors'] += 1
                logging.error(f"Error processing record: {e}")

            self.stats['processed'] += 1

        return results

    def _create_record(self, data: Dict) -> DataRecord:
        """从字典创建 DataRecord 对象"""
        return DataRecord(
            id=data.get('id', ''),
            content=data.get('content', ''),
            timestamp=datetime.now(),
            metadata=data.get('metadata', {})
        )

    def get_statistics(self) -> Dict[str, Any]:
        """获取处理统计信息"""
        return {
            **self.stats,
            'success_rate': self.stats['valid'] / max(self.stats['processed'], 1),
            'validation_count': self.validator.validation_count
        }


def main():
    """
    主函数 - 演示数据处理流程

    这个示例展示了完整的处理流水线
    """
    # 模拟输入数据
    raw_data = [
        {
            'id': '001',
            'content': '  Hello World  ',
            'metadata': {'source': 'test'}
        },
        {
            'id': '002',
            'content': 'Python Data Processing',
            'metadata': {'source': 'demo'}
        },
        {
            'id': '003',
            'content': 'Short',  # 这个会被过滤掉
            'metadata': {}
        }
    ]

    # 创建流水线
    pipeline = DataPipeline()

    # 处理数据
    results = pipeline.process(raw_data)

    # 输出结果
    print(f"处理了 {len(results)} 条有效记录")
    for record in results:
        print(f"ID: {record.id}, Content: {record.content}")

    # 打印统计
    stats = pipeline.get_statistics()
    print(f"\n统计信息: {json.dumps(stats, indent=2)}")


if __name__ == '__main__':
    main()
