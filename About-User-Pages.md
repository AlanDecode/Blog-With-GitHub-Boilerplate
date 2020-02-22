由于目前形如 `<用户名.github.io>` 的仓库只能使用 master 分支作为发布源，因此需要作出一定修改。

1. 修改仓库名为 `<用户名.github.io>` 的形式
2. 在 conf.py 中将 `site_prefix` 修改为 `"/"`

2. 修改 .github/workflows/ci.yml 第 55 行为 `PUBLISH_BRANCH: master`

4. 如果启用 jsDelivr，那么 conf.py 中 enable_jsdelivr -> repo 选项要对应设置为 `<用户名>/<仓库名>@master`

