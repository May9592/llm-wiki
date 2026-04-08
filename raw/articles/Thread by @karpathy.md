---
type: "article"
source_url: "https://x.com/karpathy/status/2039805659525644595?s=46"
author:
  - "@karpathy"
published: 2026-04-03
ingested_at: 2026-04-08
tags:
  - "clippings"
---
# Thread by @karpathy

> [原文链接](https://x.com/karpathy/status/2039805659525644595?s=46)

## 摘要

**Andrej Karpathy** @karpathy [2026-04-02](https://x.com/karpathy/status/2039805659525644595)

LLM Knowledge Bases  
法学硕士知识库  
  
Something I'm finding very useful recently: using LLMs to build personal knowledge bases for various topics of research interest. In this way, a large fraction of my recent token throughput is going less into manipulating code, and more into manipulating knowledge (stored as markdown and images). The latest LLMs are quite good at it. So:  
最近我发现一个非常有用的方法：使用 LLM 构建个人知识库，涵盖各种我感兴趣的研究主题。这样一来，我最近的大部分 token 吞吐量就不再用于操作代码，而是更多地用于操作知识（以 Markdown 和图像的形式存储）。最新的 LLM 在这方面表现相当出色。所以：  
  
Data ingest:

I index source documents (articles, papers, repos, datasets, images, etc.) into a raw/ directory, then I use an LLM to incrementally "compile" a wiki, which is just a collection of .md files in a directory structure. The wiki includes summaries of all the data in raw/, backlinks, and then it categorizes data into concepts, writes articles for them, and links them all. To convert web articles into .md files I like to use the Obsidian Web Clipper extension, and then I also use a hotkey to download all the related images to local so that my LLM can easily reference them.  
数据摄取：

我将源文档（文章、论文、代码库、数据集、图片等）索引到 raw/ 目录中，然后使用 LLM 逐步“编译”一个 wiki，它实际上就是一个目录结构中的 .md 文件集合。该 wiki 包含 raw/ 目录中所有数据的摘要、反向链接，然后将数据按概念分类，为每个概念撰写文章，并将它们链接起来。为了将网页文章转换为 .md 文件，我喜欢使用 Obsidian Web Clipper 扩展程序，然后我还使用快捷键将所有相关的图片下载到本地，以便我的 LLM 可以轻松引用它们。  
  
IDE:

I use Obsidian as the IDE "frontend" where I can view the raw data, the the compiled wiki, and the derived visualizations. Important to note that the LLM writes and maintains all of the data of the wiki, I rarely touch it directly. I've played with a few Obsidian plugins to render and view data in other ways (e.g. Marp for slides).  
IDE：

我使用 Obsidian 作为 IDE 的“前端”，可以在这里查看原始数据、编译后的 wiki 以及生成的各种可视化图表。需要注意的是，所有 wiki 数据都由 LLM 负责写入和维护，我很少直接修改。我还尝试过一些 Obsidian 插件，以其他方式渲染和查看数据（例如，使用 Marp 制作幻灯片）。  
  
Q&A:

Where things get interesting is that once your wiki is big enough (e.g. mine on some recent research is ~100 articles and ~400K words), you can ask your LLM agent all kinds of complex questions against the wiki, and it will go off, research the answers, etc. I thought I had to reach for fancy RAG, but the LLM has been pretty good about auto-maintaining index files and brief summaries of all the documents and it reads all the important related data fairly easily at this ~small scale.  
问答环节：

有趣的是，一旦你的维基足够大（例如，我最近的研究维基大约有 100 篇文章，40 万字），你就可以向你的 LLM 代理提出各种针对维基的复杂问题，它会自动去查找答案等等。我原以为我需要使用复杂的 RAG 系统，但 LLM 在自动维护索引文件和所有文档的简要摘要方面做得相当不错，而且在这个小规模下，它也能相当轻松地读取所有重要的相关数据。  
  
Output:

Instead of getting answers in text/terminal, I like to have it render markdown files for me, or slide shows (Marp format), or matplotlib images, all of which I then view again in Obsidian. You can imagine many other visual output formats depending on the query. Often, I end up "filing" the outputs back into the wiki to enhance it for further queries. So my own explorations and queries always "add up" in the knowledge base.  
输出：

我不想在终端里直接获取文本答案，而是喜欢让它渲染成 Markdown 文件、幻灯片（MARP 格式）或 matplotlib 图像，然后再用 Obsidian 查看。根据查询的不同，你可以想象出许多其他的可视化输出格式。通常，我会把这些输出“归档”回 wiki，以便更好地支持后续查询。这样，我的探索和查询就会不断积累到知识库中。  
  
Linting:

I've run some LLM "health checks" over the wiki to e.g. find inconsistent data, impute missing data (with web searchers), find interesting connections for new article candidates, etc., to incrementally clean up the wiki and enhance its overall data integrity. The LLMs are quite good at suggesting further questions to ask and look into.  
棉絮：

我使用 LLM 对维基百科进行了一些“健康检查”，例如查找不一致的数据、填补缺失数据（通过网络搜索）、寻找与新文章候选相关的有趣联系等等，以逐步清理维基百科并提高其整体数据完整性。LLM 非常擅长提出需要进一步探讨的问题。  
  
Extra tools:

I find myself developing additional tools to process the data, e.g. I vibe coded a small and naive search engine over the wiki, which I both use directly (in a web ui), but more often I want to hand it off to an LLM via CLI as a tool for larger queries.  
额外工具：

我发现自己正在开发额外的工具来处理数据，例如，我根据 wiki 编写了一个小型而简单的搜索引擎，我既可以直接使用它（在 Web 用户界面中），但更多时候，我希望通过 CLI 将其交给 LLM 作为处理更大查询的工具。  
  
Further explorations:

As the repo grows, the natural desire is to also think about synthetic data generation + finetuning to have your LLM "know" the data in its weights instead of just context windows.  
进一步探索：

随着代码库的增长，自然而然地会想要考虑合成数据生成和微调，以便让你的 LLM“了解”其权重中的数据，而不仅仅是上下文窗口。  
  
TLDR: raw data from a given number of sources is collected, then compiled by an LLM into a .md wiki, then operated on by various CLIs by the LLM to do Q&A and to incrementally enhance the wiki, and all of it viewable in Obsidian. You rarely ever write or edit the wiki manually, it's the domain of the LLM. I think there is room here for an incredible new product instead of a hacky collection of scripts.  
简而言之：系统会收集来自多个数据源的原始数据，然后由 LLM（生命周期管理）将其编译成.md 格式的 wiki 文档，之后 LLM 会通过各种命令行界面（CLI）对 wiki 进行操作，以进行问答并逐步完善 wiki，所有内容都可以在 Obsidian 中查看。您几乎不需要手动编写或编辑 wiki，这完全由 LLM 负责。我认为这里完全可以开发出一款出色的新产品，而不是一堆简陋的脚本。

## 核心观点


## 术语/概念


## 疑问/待验证