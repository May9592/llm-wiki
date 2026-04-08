"""
Knowledge Base Compiler
编译知识库的核心模块，负责将原始资料转换为结构化知识。

主要功能：
- 读取原始文档（articles, papers, discussions）
- 生成摘要和概念条目
- 维护双向链接系统
- 更新索引文件

Design Principles:
- 增量编译：只处理变更的文件
- 可追溯性：每个知识条目都有来源
- 一致性：自动检测矛盾和冲突
"""

from pathlib import Path
from typing import Dict, List, Optional
import json
from datetime import datetime


class DocumentReader:
    """文档读取器，支持多种格式"""

    SUPPORTED_FORMATS = ['.md', '.txt', '.json']

    def __init__(self, source_dir: Path):
        self.source_dir = source_dir
        self.cache = {}  # NOTE: 使用缓存避免重复读取

    def read_document(self, filepath: Path) -> Dict:
        """读取单个文档，返回结构化数据"""
        # TODO: 支持更多格式（PDF, DOCX等）
        if filepath.suffix not in self.SUPPORTED_FORMATS:
            raise ValueError(f"Unsupported format: {filepath.suffix}")

        # IMPORTANT: 保持原文不变，只读不写
        content = filepath.read_text(encoding='utf-8')

        # HACK: 临时处理 YAML frontmatter
        metadata, body = self._parse_frontmatter(content)

        return {
            'path': str(filepath),
            'metadata': metadata,
            'content': body,
            'format': filepath.suffix
        }

    def _parse_frontmatter(self, content: str) -> tuple:
        """解析 Markdown 的 YAML frontmatter"""
        lines = content.split('\n')
        if not lines[0].startswith('---'):
            return {}, content

        # 查找结束标记
        end_idx = 0
        for i, line in enumerate(lines[1:], 1):
            if line.startswith('---'):
                end_idx = i
                break

        # 提取 YAML 和正文
        yaml_text = '\n'.join(lines[1:end_idx])
        body = '\n'.join(lines[end_idx + 1:])

        # 简化的 YAML 解析（实际应该用 yaml 库）
        metadata = {}
        for line in yaml_text.split('\n'):
            if ':' in line:
                key, value = line.split(':', 1)
                metadata[key.strip()] = value.strip()

        return metadata, body


class SummaryGenerator:
    """摘要生成器，创建文档的简洁概述"""

    def __init__(self, template_path: Optional[Path] = None):
        self.template = self._load_template(template_path)

    def generate(self, document: Dict) -> Dict:
        """生成摘要，提取核心信息"""
        content = document['content']

        # 分析内容
        sections = self._extract_sections(content)
        key_points = self._extract_key_points(content)
        concepts = self._extract_concepts(content)

        return {
            'tldr': self._generate_tldr(content),
            'core_conclusions': key_points[:5],  # 最多5个核心结论
            'sections': sections,
            'concepts': concepts,
            'questions': self._generate_questions(content)
        }

    def _extract_sections(self, content: str) -> List[str]:
        """提取文档结构"""
        sections = []
        for line in content.split('\n'):
            if line.startswith('#'):
                sections.append(line.strip('#').strip())
        return sections

    def _extract_key_points(self, content: str) -> List[str]:
        """提取关键点（以 - 或 * 开头的列表）"""
        points = []
        for line in content.split('\n'):
            line = line.strip()
            if line.startswith(('-', '*')) and len(line) > 2:
                points.append(line[1:].strip())
        return points

    def _extract_concepts(self, content: str) -> List[str]:
        """提取概念和术语"""
        # TODO: 使用 NLP 技术改进概念提取
        import re
        concepts = []
        for line in content.split('\n'):
            # 查找加粗文本 **concept**
            matches = re.findall(r'\*\*([^*]+)\*\*', line)
            concepts.extend(matches)
        return list(set(concepts))

    def _generate_tldr(self, content: str) -> str:
        """生成一句话总结"""
        # HACK: 简单实现 - 取第一段或第一个标题
        for line in content.split('\n'):
            line = line.strip()
            if line and not line.startswith('#'):
                return line[:100] + '...' if len(line) > 100 else line
        return "无法生成摘要"

    def _generate_questions(self, content: str) -> List[str]:
        """生成待解答的问题"""
        questions = []
        for line in content.split('\n'):
            if '?' in line and not line.startswith('#'):
                questions.append(line.strip())
        return questions

    def _load_template(self, template_path: Optional[Path]) -> str:
        """加载摘要模板"""
        # IMPORTANT: 模板应该可配置
        if template_path and template_path.exists():
            return template_path.read_text()
        return "默认摘要模板"


class ConceptExtractor:
    """概念提取器，从文档中识别和定义概念"""

    def __init__(self):
        self.existing_concepts = {}  # 已存在的概念库

    def extract(self, document: Dict, summary: Dict) -> List[Dict]:
        """从文档中提取新概念"""
        concepts = []
        concept_names = summary.get('concepts', [])

        for name in concept_names:
            if name not in self.existing_concepts:
                concept = {
                    'name': name,
                    'definitions': self._find_definitions(document['content'], name),
                    'examples': self._find_examples(document['content'], name),
                    'related_concepts': self._find_related(name, concept_names),
                    'source': document['path']
                }
                concepts.append(concept)
                self.existing_concepts[name] = concept

        return concepts

    def _find_definitions(self, content: str, concept: str) -> List[str]:
        """查找概念的定义"""
        definitions = []
        for line in content.split('\n'):
            if concept.lower() in line.lower() and ('是' in line or '定义' in line):
                definitions.append(line.strip())
        return definitions

    def _find_examples(self, content: str, concept: str) -> List[str]:
        """查找概念的例子"""
        examples = []
        # TODO: 改进例子查找算法
        for line in content.split('\n'):
            if '例子' in line or 'example' in line.lower():
                examples.append(line.strip())
        return examples[:3]  # 最多3个例子

    def _find_related(self, concept: str, all_concepts: List[str]) -> List[str]:
        """查找相关概念"""
        # HACK: 简单实现 - 基于共现
        related = []
        for other in all_concepts:
            if other != concept:
                related.append(other)
        return related


class KnowledgeCompiler:
    """知识库编译器，协调整个编译流程"""

    def __init__(self, source_dir: Path, output_dir: Path):
        self.source_dir = source_dir
        self.output_dir = output_dir
        self.reader = DocumentReader(source_dir)
        self.summary_generator = SummaryGenerator()
        self.concept_extractor = ConceptExtractor()

        # 状态跟踪
        self.compiled_files = set()
        self.manifest_path = output_dir / 'manifest.json'

    def compile(self, incremental: bool = True) -> Dict:
        """执行编译流程"""
        # 读取上次的 manifest
        previous_manifest = self._load_manifest() if incremental else {}

        # 查找需要处理的文件
        files_to_process = self._get_files_to_process(previous_manifest)

        results = {
            'processed': 0,
            'summaries': 0,
            'concepts': 0,
            'errors': []
        }

        # 处理每个文件
        for filepath in files_to_process:
            try:
                result = self._compile_file(filepath)
                results['processed'] += 1
                results['summaries'] += result['summaries']
                results['concepts'] += result['concepts']
                self.compiled_files.add(str(filepath))
            except Exception as e:
                results['errors'].append({
                    'file': str(filepath),
                    'error': str(e)
                })

        # 更新 manifest
        self._save_manifest()

        return results

    def _get_files_to_process(self, previous_manifest: Dict) -> List[Path]:
        """获取需要处理的文件列表"""
        all_files = []
        for ext in DocumentReader.SUPPORTED_FORMATS:
            all_files.extend(self.source_dir.rglob(f'*{ext}'))

        if not previous_manifest:
            return all_files

        # 增量编译：只处理变更的文件
        to_process = []
        for filepath in all_files:
            mtime = filepath.stat().st_mtime
            cached = previous_manifest.get(str(filepath), {}).get('mtime')
            if not cached or mtime > cached:
                to_process.append(filepath)

        return to_process

    def _compile_file(self, filepath: Path) -> Dict:
        """编译单个文件"""
        # 读取文档
        document = self.reader.read_document(filepath)

        # 生成摘要
        summary = self.summary_generator.generate(document)

        # 提取概念
        concepts = self.concept_extractor.extract(document, summary)

        # 保存结果
        summary_path = self._save_summary(filepath, summary)
        concept_paths = [self._save_concept(c) for c in concepts]

        return {
            'summaries': 1,
            'concepts': len(concepts),
            'summary_path': str(summary_path),
            'concept_paths': [str(p) for p in concept_paths]
        }

    def _save_summary(self, source_path: Path, summary: Dict) -> Path:
        """保存摘要到 wiki/summaries/"""
        # 生成文件名
        filename = f"S-{self._next_number()}-{source_path.stem}.md"
        output_path = self.output_dir / 'summaries' / filename

        # 格式化为 Markdown
        content = self._format_summary(source_path, summary)
        output_path.write_text(content, encoding='utf-8')

        return output_path

    def _save_concept(self, concept: Dict) -> Path:
        """保存概念到 wiki/concepts/"""
        filename = f"C-{self._next_number()}-{concept['name']}.md"
        output_path = self.output_dir / 'concepts' / filename

        content = self._format_concept(concept)
        output_path.write_text(content, encoding='utf-8')

        return output_path

    def _format_summary(self, source_path: Path, summary: Dict) -> str:
        """格式化摘要为 Markdown"""
        return f"""---
type: summary
source: [[{source_path}]]
compiled_at: {datetime.now().isoformat()}
status: done
---

# {self._next_number()}: {source_path.stem}

## TL;DR
{summary['tldr']}

## 核心结论
{chr(10).join(f"- {point}" for point in summary['core_conclusions'])}

## 关键证据
{chr(10).join(f"- {section}" for section in summary['sections'])}

## 概念提取
{chr(10).join(f"- [[{concept}]]" for concept in summary['concepts'])}

## 疑点/待验证
{chr(10).join(f"- {q}" for q in summary['questions'])}
"""

    def _format_concept(self, concept: Dict) -> str:
        """格式化概念为 Markdown"""
        return f"""---
type: concept
source: [[{concept['source']}]]
compiled_at: {datetime.now().isoformat()}
---

# {concept['name']}

## 定义
{chr(10).join(f"- {d}" for d in concept['definitions'])}

## 例子
{chr(10).join(f"- {e}" for e in concept['examples'])}

## 相关概念
{chr(10).join(f"- [[{r}]]" for r in concept['related_concepts'])}

## 来源
[[{concept['source']}]]
"""

    def _next_number(self) -> int:
        """获取下一个编号"""
        # HACK: 简单实现 - 实际应该从现有文件中获取最大编号
        return len(self.compiled_files) + 1

    def _load_manifest(self) -> Dict:
        """加载上次的编译清单"""
        if self.manifest_path.exists():
            return json.loads(self.manifest_path.read_text())
        return {}

    def _save_manifest(self):
        """保存编译清单"""
        manifest = {}
        for filepath_str in self.compiled_files:
            filepath = Path(filepath_str)
            manifest[filepath_str] = {
                'mtime': filepath.stat().st_mtime,
                'compiled_at': datetime.now().isoformat()
            }
        self.manifest_path.write_text(json.dumps(manifest, indent=2))


def main():
    """主函数 - 编译知识库"""
    source = Path('raw/articles')
    output = Path('wiki')

    compiler = KnowledgeCompiler(source, output)
    results = compiler.compile(incremental=True)

    print(f"编译完成:")
    print(f"  处理文件: {results['processed']}")
    print(f"  生成摘要: {results['summaries']}")
    print(f"  提取概念: {results['concepts']}")
    if results['errors']:
        print(f"  错误: {len(results['errors'])}")
        for error in results['errors']:
            print(f"    {error['file']}: {error['error']}")


if __name__ == "__main__":
    main()