# 数学原理

> **本文件只讲"为什么"。所有数值一律去 [`reference/`](../reference/) 查，本文件不重复给数。**

---

## 概念地图

| 概念 | 一句话 | 数值在哪 |
| --- | --- | --- |
| 底池赔率 | 跟注需要的最低胜率 | [`reference/pot-odds.md`](../reference/pot-odds.md) |
| 弃牌权益 | 诈唬需要对手弃牌的百分比 | [`reference/pot-odds.md`](../reference/pot-odds.md) |
| MDF | 面对下注至少要防守的比例 | [`reference/mdf.md`](../reference/mdf.md) |
| 权益 | 当前胜率 | [`reference/equity.md`](../reference/equity.md) |
| 组合数 | 某范围有多少种牌 | [`reference/combinatorics.md`](../reference/combinatorics.md) |
| SPR | 筹码 ÷ 底池 | [`reference/spr.md`](../reference/spr.md) |

---

## 三个最该理解的思想

### 1. 赔率决定跟不跟

你的胜率 > 底池赔率要求的胜率 → 跟。见 [`reference/pot-odds.md`](../reference/pot-odds.md)。

### 2. 对手下小注，你不能轻易弃

MDF = `底池 ÷ (底池 + 下注)`。对手下得越小，MDF 越高（要求你防守越多）。

**依据**：否则对手用任意两张牌诈唬都能盈利。`[数学]`

**但**：MDF 成立的前提是"对手真的会诈唬"。对手不诈唬时，可以弃得比 MDF 多（这是剥削）。见 [`reference/mdf.md`](../reference/mdf.md)。

### 3. 权益 ≠ 能赢到的钱

**实现权益**：位置好、有主动权 → 能兑现的权益超过账面值；位置差、被压制 → 兑现不足。

**意义**：`KQ` 在 BB 防守后翻后很难打，因为账面权益看着不差，但实现率低。`[共识]`

---

## EV：把决策写成期望

**跟注的 EV** = 胜率 × (底池 + 对手下注) − 败率 × 跟注额

结果 > 0 → 有利。这是所有决策的最终判据。`[数学]`

---

## ICM（锦标赛）

筹码的**边际价值递减**——筹码越多，每枚的美元价值越低。

**推论**：不要为了轻微的 +chip EV 去冒被淘汰的风险。`[共识]`
**应用**：泡沫期、决赛桌的跟注范围要收缩。详见 [`07-formats/mtt.md`](../07-formats/mtt.md)。

---

## 本文件不做什么

- **不给数值**——全部在 [`reference/`](../reference/)。
- **不算具体牌局**——需要精确数值时，agent 应查表；表未覆盖则说明无法给出。
