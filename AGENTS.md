# AGENTS.md — 知识库使用说明

**你是来使用这个知识库的 AI agent。先读完本页，再取用具体文件。**

本库是关于德州扑克策略的结构化知识库。它不为人类阅读体验优化，而为**你的正确使用**优化。下面三条铁律决定了你能不能用对。

> **要出一个具体的打法决策时**：直接走 [`DECISION.md`](DECISION.md)——那是从牌局处境到动作的完整四步流程。本页讲的是"怎么正确使用这个库"，`DECISION.md` 讲的是"怎么走完一次决策"。

---

## 铁律一：不要心算，去查表

**本库所有数值结论都已预计算，存放在 [`reference/`](reference/)。**

只要你需要下面任何一项，**必须查表，不要自己推导**：

| 你需要 | 查哪张表 |
| --- | --- |
| 跟注需要多少胜率 / 该不该跟 | [`reference/pot-odds.md`](reference/pot-odds.md) |
| 面对下注该防守多少比例 | [`reference/mdf.md`](reference/mdf.md) |
| 诈唬需要对手弃牌多少比例 | [`reference/pot-odds.md`](reference/pot-odds.md) |
| 某个听牌的胜率 | [`reference/equity.md`](reference/equity.md) |
| 对手范围里有多少种组合 | [`reference/combinatorics.md`](reference/combinatorics.md) |
| 该下多大 / 能不能打光 | [`reference/spr.md`](reference/spr.md) |

> **查不到怎么办**：回复"本库未覆盖这一项，我不能确定"。**绝对不要自己算。**
>
> 你的心算会出错，而在扑克里算错赔率会直接导致输钱。宁可说不知道。

---

## 铁律二：不要通读，按路由取用

你**不应该**读完整个知识库。按用户的处境，只读需要的那几个文件。

| 用户的处境的 | 先读 | 需要时再读 |
| --- | --- | --- |
| **要出一个打法决策** | [`DECISION.md`](DECISION.md) | 按流程走到底 |
| 翻前要不要入池 | [`01-preflop/ranges.md`](01-preflop/ranges.md) | |
| 翻前被人加注 / 被 3-bet | [`01-preflop/facing-raise.md`](01-preflop/facing-raise.md) | |
| 盲注要不要防守 | [`01-preflop/facing-raise.md`](01-preflop/facing-raise.md) | |
| 翻牌该不该下注 | [`02-postflop/cbet-and-barrels.md`](02-postflop/cbet-and-barrels.md) | [`02-postflop/board-texture.md`](02-postflop/board-texture.md) |
| 面对下注，跟还是弃 | [`reference/pot-odds.md`](reference/pot-odds.md) | [`reference/equity.md`](reference/equity.md) |
| 该不该诈唬 | [`reference/pot-odds.md`](reference/pot-odds.md) | `02-postflop/` |
| 该下多大尺度 | [`03-betting-sizing/README.md`](03-betting-sizing/README.md) | [`reference/spr.md`](reference/spr.md) |
| 这个牌面算干燥还是湿润 | [`02-postflop/board-texture.md`](02-postflop/board-texture.md) | |
| 对手是什么类型、怎么针对 | [`05-exploits/README.md`](05-exploits/README.md) | |
| 锦标赛 / 泡沫期 / ICM | [`07-formats/mtt.md`](07-formats/mtt.md) | |
| 资金管理 / 心态 / 上头 | [`06-mental-bankroll/README.md`](06-mental-bankroll/README.md) | |
| 某个名词不懂 | [`GLOSSARY.md`](GLOSSARY.md) | |
| 某个玩法的特殊规则 | [`07-formats/`](07-formats/) | |

---

## 铁律三：条件不满足，规则不适用

本库每条规则都带**条件**。**条件缺一不可**——不能把"有位置时的打法"用到无位置上。

读规则前先确认你手上有全部条件。**条件不全时，先问用户缺什么，或者明说这条不能套用。**

---

## 规则怎么读

各模块的规则统一是这种格式：

| 位置 | 筹码深度 | 牌面 / 场景 | 面对 | 动作 | 尺度 | 依据 | 置信度 |
| --- | --- | --- | --- | --- | --- | --- | --- |
| BTN | 100bb | 翻前 | CO open | 3-bet 或弃 | 3× | 阻断 + 翻后可打 | `[共识]` |

- **牌面 / 场景**：引用 [`02-postflop/board-texture.md`](02-postflop/board-texture.md) 的定义（干燥 / 湿润 / 连接 / 同花 / 成对）
- **动作**：open / 3-bet / c-bet / check-raise / fold / call / all-in 等，见 [`GLOSSARY.md`](GLOSSARY.md)
- **依据**：为什么
- **置信度**：见下

### 置信度标记

| 标记 | 含义 | 你该怎么用 |
| --- | --- | --- |
| `[数学]` | 可验证的数学结论（赔率、概率） | 可信，直接引用 |
| `[共识]` | 主流公认的策略 | 可信，正常引用 |
| `[常见]` | 常见打法，但存在流派差异 | 引用时说明"这是常见打法之一" |
| `[经验]` | 实战经验，未经严格验证 | 引用时说明不确定 |
| `[存疑]` | 有争议或可能过时 | 明确告诉用户需自行验证 |

---

## 本库覆盖什么、不覆盖什么

**覆盖：**
- 翻前范围与行动线、翻后牌面判断与下注、下注尺度与底池几何
- 数学：赔率、权益、组合数、MDF、EV、SPR（全部在 `reference/`）
- 对手类型识别与针对性打法
- 心态、资金管理、复盘方法
- 六种玩法：6-max 现金、满员现金、MTT、SNG、单挑、短牌

**不覆盖（不要假装知道）：**
- 实时读取牌桌 / 操作客户端——本库只是知识，不含任何工具或接口
- 具体某个平台、某个赛事、某个对手的历史数据
- 精确的求解器输出——本库范围是**近似起点**，不是 GTO 精确解
- 任何需要实时计算而表里没给的情况

> **范围表是起点，不是真理。** 遇到强对手或非常规局面，应提醒用户这些是标准打法、需要按对手调整。

---

## 回答用户时

1. **给动作，也给条件**：不要只说"这里该 3-bet"，要带上位置、筹码、面对的动作。
2. **数值只从 `reference/` 取**，引用哪张表就说哪张。
3. **说清楚置信度**：`[共识]` 就说共识，`[经验]` 就承认是经验。
4. **不确定就说不确定**：这是本库最重要的要求。瞎编一个范围比说"我不确定"危害大得多。
5. **不适用范围要提示**：如果局面超出了本库的覆盖（比如极深筹码、特殊规则），明说。

---

## 目录结构

```
AGENTS.md            ← 本文件，agent 入口
DECISION.md          ← ★ 决策流程：处境 → 动作的完整四步
README.md            ← 面向人的项目说明
GLOSSARY.md          ← 术语与范围记号定义（读任何模块前建议先扫一眼）
reference/           ← 预计算表。唯一数字来源
01-preflop/          ← 翻前
02-postflop/         ← 翻后
03-betting-sizing/   ← 下注尺度
04-math-odds/        ← 数学原理（数值在 reference/）
05-exploits/         ← 读人与剥削
06-mental-bankroll/  ← 心态与资金
07-formats/          ← 六种玩法
08-tools/            ← 工具
```
