pre-commit在balck自动格式化之后依然认为本次检查是错误的
pre-commit认为只是一个检查工具，不应该对暂存代码有任何修改提交操作，所以刻意保持了这个限制
参考issue: https://github.com/pre-commit/pre-commit/issues/747#issuecomment-386782080

---

prettier配置
```
types: [file]
files: "\\.(py|json)$"
```
参考issue: https://github.com/prettier/prettier/issues/2745

---

添加precommit hooks
需要在项目根目录下添加.precommit.yaml配置文件
参考: https://pre-commit.com/#new-hooks

---

对于一些知名的但是没有添加hooks的检查项目，作者添加了mirror-project来支持

---

pylint报错
Unable to import xxx
因为precommit是在一个独立的虚拟环境中运行，所以虚拟环境中没有的包就会报错
所以推荐pylint使用本地的方式进行检查

参考网址: https://github.com/pre-commit/mirrors-pylint/blob/master/README.md

---

isort 和 black有冲突：
isort对一些主流的框架都写了适配的文件，直接使用--profile 参数即可

参考网址:https://pycqa.github.io/isort/docs/configuration/profiles/

---
stages
通过设置manual可以使在普通运行时不使用此工具检查，仅仅单独跑`pre-commit run --hook-stage manual [hookid]`才会检查


default_stages: [commit, merge-commit]
