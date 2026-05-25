# GitHub Pages Agent 生态地图升级计划

## 目标

把 GitHub Pages 从“README 的网页镜像”升级成“可探索的 Agent 生态地图”。

页面应该让读者快速理解 `awsome agent hierarchy` 的整体结构，并能按层级、主题、标签、仓库类型浏览内容。同时，README 与 Pages 要保持统一的视觉气质，中文与英文切换不能出现乱码。

## 当前问题

- 首页更像目录卡片，缺少强主视觉和项目识别度。
- `docs/index.html` 和部分生成页面里可能存在中文乱码，例如 `涓枃`、`鍩虹灞` 一类内容。
- GitHub 链接需要统一指向当前公开仓库：`https://github.com/GoDiao/awsome-agent-hierarchy`。
- 首页不能直接搜索全部仓库，用户必须先进入具体 layer。
- 每层卡片比较单薄，缺少图标、统计、主题提示和视觉层级。
- Layer 页面以文字列表为主，缺少清晰的 section header、repo card 和当前位置导航。
- `Large Language Models / Providers` 不是普通 GitHub repo 列表，不适合把 provider 和模型全部平铺展示。

## 第一阶段：高性价比基础升级

### 1. 首页使用框架图作为主视觉

在 `docs/index.html` 首页首屏展示 `docs/awesome-agent-hierarchy.png`。

要求：

- 框架图作为首页 hero visual，而不是只出现在 README。
- 图片在桌面端和移动端都不能溢出。
- 图片下方继续展示 8 个 layer card。
- README 与 GitHub Pages 形成统一视觉识别。

验收标准：

- 打开首页第一眼能看到完整的 Agent 生态框架图。
- 移动端图片比例正常，文字不被裁切到不可读。

### 2. 修复 docs 中文乱码

检查 `generate.py` 和已生成的 `docs/*.html`，确保所有中文内容以 UTF-8 正确输出。

重点排查：

- 语言切换按钮。
- 中文 layer 名称。
- 中文 topic 标题。
- README 解析后进入页面的中文描述。
- 常见乱码残留，例如 `涓`、`鍩`、`閸`、`锟`、`�`。

验收标准：

- 首页和所有 layer 页面中文显示正常。
- 后续运行生成脚本不会重新引入乱码。

### 3. 更新 GitHub 仓库链接

把 docs 页面中的旧链接：

```text
https://github.com/tianX-ai/awsome-agent-hierarchy
```

统一替换为：

```text
https://github.com/GoDiao/awsome-agent-hierarchy
```

验收标准：

- 首页和所有 layer 页导航里的 GitHub 链接都指向当前公开仓库。
- 页面中不再残留旧仓库地址。

### 4. 首页增加全局统计

在首页 hero 下方增加一组紧凑统计：

- `8 Layers`
- `51 Topics`
- `510 Repos`
- `6 Tags`

要求：

- 优先从 README / 解析数据中动态计算。
- 统计信息不要喧宾夺主，只作为项目规模感提示。

验收标准：

- 用户能立刻感受到这是一个有规模、有结构的数据地图。

## 第二阶段：视觉和信息层级增强

### 5. 首页 layer card 升级

把首页卡片从纯文字入口升级为更容易扫读的地图节点。

建议：

- 每个 layer 增加一个 icon。
- 每个 layer 分配一个 accent color。
- 卡片展示 topic 数量和 repo 数量，例如 `Foundation Layer · 13 sections · 80 repos`。
- 卡片展示 2 到 4 个核心子类 chips。
- `Infrastructure`、`Observability`、`Security` 可以作为 supporting layers，在视觉上和中间 5 层略作区分。

验收标准：

- 首页不再显得空和单薄。
- 用户不用点进页面，也能大致理解每层覆盖什么内容。

### 6. Layer 页面顶部升级

每个 layer 页面顶部增加更明确的 header 区域。

建议内容：

- layer icon。
- layer 中英文名称。
- 一句简短说明。
- topic 数量和 repo 数量。
- mini layer nav，让用户知道当前位于 8 层结构中的哪一层。

验收标准：

- 每个页面都像“生态地图的一个区域”，而不是 markdown 列表镜像。

### 7. Topic 增加展开与收起控制

每个 layer 页面增加：

- `Expand all`
- `Collapse all`
- 默认展开第一个 topic。

验收标准：

- 用户进入页面后能直接看到第一组内容。
- 用户可以快速展开全部内容做浏览，也可以收起全部内容重新定位。

## 第三阶段：内容组件优化

### 8. LLM Provider 使用两级折叠

`Commercial / Cloud Providers` 和 `Open-Source / Open-Weight Providers` 不应按普通 repo list 平铺。

建议结构：

```text
Commercial / Cloud Providers
  OpenAI              5 models     collapsed
  Anthropic           5 models     collapsed
  Google DeepMind     5 models     collapsed
  Mistral AI          5 models     collapsed

Open-Source / Open-Weight Providers
  Meta                5 models     collapsed
  DeepSeek            5 models     collapsed
  Qwen                5 models     collapsed
```

Provider 展开后示例：

```text
OpenAI
[GPT-5.5] flagship reasoning/coding
[GPT-5.4] affordable frontier
[GPT-5.4 mini] fast subagent model
```

交互要求：

- 默认只展开每个 provider group 的第一个 provider。
- 其他 provider 默认隐藏。
- 提供 `Expand all providers` / `Collapse all providers`。

验收标准：

- Foundation Layer 明显更容易扫读。
- Provider 和 GitHub repo topic 在视觉与交互上有明确区别。

### 9. Repo list 做轻量 repo card

把普通列表增强成轻量 repo card 或增强列表行。

每项建议展示：

- repo 名称。
- 一句话描述。
- tag chips。
- stars badge。
- official / framework / example / research / infra / archived classic 等类型提示。

验收标准：

- 仍然保持 awesome list 的密度。
- 信息分区比纯文本列表更清楚。
- 页面不会因为卡片过重而显得慢或杂乱。

## 第四阶段：搜索、筛选与贡献入口

### 10. 首页增加全站搜索

首页增加 `Search all repositories` 输入框。

建议能力：

- 跨全部 layer 搜索 repo 名称和描述。
- 搜索结果可以在首页直接展示。
- 或跳转到对应 layer 并携带 query 参数。

验收标准：

- 用户不需要先理解层级，也能直接找到目标仓库。

### 11. 标签筛选升级为跨层导航

把当前 layer 内标签筛选提升为首页入口。

标签包括：

- `Official`
- `Framework`
- `Example`
- `Research`
- `Infra`
- `Archived Classic`

验收标准：

- 用户可以从标签维度探索整个 Agent 生态，而不仅是某一层。

### 12. 增加 Submit a Repo 入口

在首页和导航中加入贡献入口。

建议：

- 链接到 `CONTRIBUTING.md`。
- 后续可以增加 GitHub issue template。

验收标准：

- 读者能明显看到如何提交新仓库。
- 项目更像可持续维护的 awesome list。

## 第五阶段：分享与性能 polish

### 13. 增加 SEO 和 Open Graph

为 Pages 增加基础 metadata：

- `title`
- `description`
- `og:title`
- `og:description`
- `og:image`

`og:image` 使用框架图。

验收标准：

- 链接被分享到社交平台时有清晰标题、描述和预览图。

### 14. 压缩首页框架图

当前框架图约 1.49 MB，可以接受，但作为首页主视觉偏重。

建议：

- 尝试压缩到 300 到 700 KB。
- 如果压缩明显损害图中文字可读性，则保留原图。

验收标准：

- 首页加载更轻。
- 框架图文字仍然清晰可读。

## 实现原则

- 不引入 React。
- 不引入构建系统。
- 继续使用 `generate.py`、静态 HTML、CSS 和 vanilla JS。
- 图标优先使用生成器内置 inline SVG。
- 每层使用独立 accent color。
- 页面保持 GitHub Pages 友好，加载快，结构清晰。
- 不做过度营销化设计，目标是“可浏览的生态地图”，不是 landing page。

## 建议首个交付版本

第一版建议只做小而稳的升级：

1. 修复 docs 中文乱码。
2. 更新 GitHub URL。
3. 首页加入框架图。
4. 首页加入全局统计。
5. 首页 layer card 加 icon、颜色和 chips。
6. 每个 topic 增加 `Expand all` / `Collapse all`。
7. LLM provider 改成可展开 / 隐藏。
8. repo list 做轻量视觉增强。

完成这组改动后，页面会从“文字目录”升级成“可浏览的生态地图”，同时仍然保持当前静态站点的简单维护方式。
