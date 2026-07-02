
# bazi-analysis-skill

一个中文八字分析 Agent Skill，可用于 Codex、Claude、Trae、腾讯 Workbuddy 等支持 Skill / Agent / Knowledge / Tool 导入能力的 AI Agent。

本 Skill 用于根据出生信息进行八字排盘与命理分析，支持分析命局结构、旺衰、用神喜忌、大运流年、事业、财运、婚姻、健康等内容。

> 本项目属于传统命理文化分析工具，仅供参考，不应作为投资、医疗、法律、婚姻等重大决策的唯一依据。

## 如何安装

最简单的方式是：复制本 GitHub 仓库链接，然后发送给你正在使用的 Agent。

仓库链接：

```text
https://github.com/maochengsun16-code/bazi-analysis-skill
```

你可以在 Codex、Claude、Trae、腾讯 Workbuddy 等 Agent 中这样说：

```text
请帮我从这个 GitHub 仓库安装 bazi-analysis skill：
https://github.com/maochengsun16-code/bazi-analysis-skill

安装后请读取其中的 bazi-analysis/SKILL.md，并在我提问八字分析问题时使用这个 skill。
```

如果你的 Agent 支持从 GitHub 导入 Skill，它会自动读取仓库并安装。

如果你的 Agent 不支持自动安装，可以手动下载本仓库，然后把 `bazi-analysis/` 文件夹导入到对应 Agent 的 Skill、Knowledge、Tool 或自定义能力目录中。

## 使用前必须知道

八字分析必须提供**具体出生时间**，也就是出生时辰。

只提供出生年月日是不够的。例如：

```text
2026年7月2日
```

这个信息不完整，无法准确排出完整四柱。

至少要写成：

```text
2026年7月2日 凌晨3点半
```

或者：

```text
2026年7月2日 寅时
```

如果不知道准确分钟，也应尽量提供大概时辰，例如：

```text
早上7点左右
下午3点到5点之间
晚上9点多
```

没有出生时间时，Skill 只能做非常有限的参考分析，不能进行完整八字判断。

## 安装后如何提问

安装完成后，可以直接按照下面模板提问：

```text
请使用 bazi-analysis skill 分析这个八字：

性别：男 / 女
历法：阳历 / 农历
出生日期：****年**月**日
出生时间：**点**分 / **时
重点问题：未来五年的财运 / 现在单身，什么时候能遇到正缘 / 事业发展如何
```

也可以简化成一句话：

```text
使用 bazi-analysis skill，帮我分析一个八字：男命 / 女命，阳历 / 农历 **** 年 ** 月 ** 日凌晨 ** 点，重点看未来五年的财运 / 现在单身，什么时候能遇到正缘 / 事业发展如何。
```

## 必须提供的信息

完整八字分析必须提供：

- 性别：男 / 女
- 历法：阳历 / 阴历
- 出生年月日
- 具体出生时间：几点几分，或明确的时辰

其中，**出生时间是必须项**。没有出生时间，就无法完整排出年柱、月柱、日柱、时柱。

## 可以分析什么

本 Skill 可以用于分析：

- 八字排盘
- 四柱结构
- 日主旺衰
- 十神关系
- 格局判断
- 用神、喜神、忌神
- 大运走势
- 流年应期
- 事业职业
- 财运财富
- 婚姻感情
- 父母子女
- 健康倾向
- 风险年份提示

## 输出内容示例

当你输入完整出生信息后，Agent 通常会输出：

```text
1. 基础排盘
   年柱、月柱、日柱、时柱

2. 命局结构
   日主强弱、月令、十神分布、五行偏重

3. 用神喜忌
   喜用方向、忌神方向、调候重点

4. 大运分析
   当前大运、未来大运走势

5. 流年分析
   指定年份或未来几年的重点变化

6. 专项分析
   财运、事业、婚姻、健康等具体问题

7. 行动建议
   适合把握的方向、需要谨慎的年份或事项
```

## 目录结构

```text
bazi-analysis/
  SKILL.md
  CLAUDE.md
  TRAE.md
  WORKBUDDY.md
  agents/
  scripts/
  references/

README.md
LICENSE
THIRD_PARTY_NOTICES.md
```

## License

This project is licensed under the MIT License.
