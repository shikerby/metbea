# METMSG

> 这个文件会详细记录项目开发的过程 .  
> *Metbea is a info-social sites that can be customized to publish information.*  
> *how happy we are, To meet friends from afar.* --

## 开发日志
- 初始化项目配置, 将项目交付github私有仓库管理
- 创建django项目的地一个app: account 
- 配置postgresql, 数据库名: db_metmsg 管理数据库: db_admin 数据库密码: db_mima
- 设置超级用户: admin 超级用户密码: admin83

## 特色功能
1. 实现用户内容 **自由定制时间** 上首页
    * 自定制时间开始持续24小时处于首页头条
    * 此后用户内容将进入自由排序,即由明文规则得到的综合评分排序,持续时间为5天
    * 再之后将进入本站全文搜索排序中,低于某一分支,在搜索结果中将不予展示
2. 实现用户明文规则约束
3. 实现发布内容的用户对评论形式的可选样式锁定

### 第一更新开发日志2019.2.21
* 自定义模板标签和实现markdown过滤器
* 为评论实现高级功能
* 实现个人页面
* 实现本站搜索功能
* 实现对每篇博客的浏览量统计