# Texas Hold'em Skill

> 面向 AI agent 的德州扑克知识库 · A Texas Hold'em knowledge base for AI agents

一个结构化的德州扑克策略知识库。**它不是给人读的教程，是给 AI agent 取用的知识源**——数字全部预计算成表、规则全部带条件、术语全部统一。

---

## 给用 agent 的人：怎么接入

1. 把你的 agent 指向 **[`AGENTS.md`](AGENTS.md)**。这是 agent 的唯一入口，里面写了三条铁律和路由表。
2. 你的 agent 会自己按 URL/路径读取所需文件。**不需要任何工具、脚本或 API**——纯 markdown，Codex、Claude Code、Cursor 或任何能读文件的 agent 都能直接用。

> 如果你的 agent 只认特定入口文件名（如 Claude Code 的 `CLAUDE.md`），把它指到 `AGENTS.md` 即可，内容通用。

---

## 为什么这样设计

LLM agent 有两个硬毛病，本库专门绕开：

| 毛病 | 表现 | 本库的解法 |
| --- | --- | --- |
| **不会算数** | 心算底池赔率、权益、组合数必错 | 全部预计算进 [`reference/`](reference/)，agent 只查不算 |
| **不会通读** | 随机访问，易从自己的记忆里瞎编 | [`AGENTS.md`](AGENTS.md) 提供路由表，一步定位 |

另外每条规则都带**条件**和**置信度标记**，让 agent 知道"这条在什么前提下成立""这条有多可信"。

---

## 结构

```
AGENTS.md            ★ agent 入口：铁律、路由表、规则格式
DECISION.md          ★ 决策流程：从牌局处境到动作的完整四步
README.md              本文件（面向人）
GLOSSARY.md            术语表 + 范围记号规范 ★ 读其他文件前建议先看
CONTRIBUTING.md        规则格式与贡献规范

reference/           ★ 预计算表，全库唯一数字来源
├── pot-odds.md          底池赔率、弃牌权益
├── mdf.md               MDF / Alpha
├── equity.md            听牌胜率、翻前对局
├── combinatorics.md     组合数、阻断牌
├── spr.md               SPR、底池几何
└── icm.md               锦标赛 ICM（含完整算例）

01-preflop/          翻前：范围、面对加注
02-postflop/         翻后：牌面判断、持续下注、面对下注、转河、多人
03-betting-sizing/   下注尺度
04-math-odds/        数学原理（数值见 reference/）
05-exploits/         读人与剥削
07-formats/          六种玩法：6-max / 满员 / MTT / SNG / 单挑 / 短牌

tests/spots.md       ★ 测点集：固定局面 + 标准动作，用来给 agent 打分
scripts/             数字校验（CI 会跑）

human/               面向人的内容，agent 做决策时用不到
├── mental-bankroll.md   心态与资金管理
└── tools.md             工具
```

---

## 置信度标记

每条规则都标了来源可信度，agent 引用时会带上：

| 标记 | 含义 |
| --- | --- |
| `[数学]` | 可验证的数学结论 |
| `[共识]` | 主流公认策略 |
| `[常见]` | 常见打法，存在流派差异 |
| `[经验]` | 实战经验，未经严格验证 |
| `[存疑]` | 有争议或可能过时 |

**本库范围表是标准起点，不是 GTO 精确解。** 遇到强对手或非常规局面，应结合对手调整。

---

## 声明

- 本库为**纯知识内容**，不含任何实时工具、接口或自动化程序。
- 内容仅供学习、复盘与研究使用。
- 请遵守你所在地的法律法规，以及任何你参与的游戏平台的服务条款。
- 不构成任何形式的赌博建议。

---

## 贡献

欢迎补充和修正。加规则前请先读 [`CONTRIBUTING.md`](CONTRIBUTING.md)（规定了规则表格式与置信度标记）。所有数值请放进 [`reference/`](reference/)，不要在模块里重复造数。

## License

[CC BY 4.0](LICENSE)
