# uniref

uniref 是一个辅助分析 Unity 应用的框架。它可以帮助您获取 Unity 应用中的类、方法、成员变量等的反射信息，让您实时地查看和操作它们。

您可以将您的一些分析结果借助本框架转化为少量的 Python 代码，在一定程度上方便您进行 Unity 应用的插件开发。

目前 uniref 支持分析 Windows x86 64 位操作系统上运行的 32 / 64 位 Unity 应用，且同时支持 `Mono` 和 `IL2CPP` 两种脚本后端（Unity scripting backend）。

## 安装

uniref 需要 Python 3.7+（64 位）的运行环境，您可以通过 pip 完成安装：

```bash
pip install -U uniref
```

## 示例

下方给出了一段使用 uniref 框架完成的代码，其实现了修改鹅鸭杀游戏人物移速的效果。

您可以在游戏的教程关卡中运行[^1]这段代码来体验 uniref，**请勿在多人模式下使用**，影响其他玩家游戏体验。

```Python
from uniref import WinUniRef

# 指定待分析进程
ref = WinUniRef("Goose Goose Duck.exe")

# 查找类
class_path = "Handlers.GameHandlers.PlayerHandlers.LocalPlayer"
local_player = ref.find_class_in_image("Assembly-CSharp.dll", class_path)

# 查找类中的成员变量，并打印其值
movement_speed = local_player.find_field("movementSpeed")
print(f"default speed: {movement_speed.value}")

# 修改成员变量的值
movement_speed.value = 20.0
```

## 下一步计划

支持 Android 平台

## 参与进来

如果您有什么建议或需求，欢迎提 [issue](https://github.com/in1nit1t/uniref/issues)。

当然，如果您有兴趣一起完善这个框架，欢迎提交 [Pull requests](https://github.com/in1nit1t/uniref/pulls)。

## 开源协议

[GNU Affero General Public License v3.0](https://github.com/in1nit1t/uniref/blob/main/LICENSE)

------

[^1]: 如果目标进程是以管理员权限启动的，那么请保证本框架运行在管理员权限下。即必要时，需要使用管理员权限运行 Python。
