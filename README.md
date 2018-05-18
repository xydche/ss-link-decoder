安卓新版Shadowsocks客户端(包名：com.github.shadowsocks)已不再支持NAT模式，用着不爽，所以转到SSR来用。一些配置需要解析出密码和加密方式，撸了这个脚本方便自己使用，仅支持**python3**。
***
# 用法
```bash
python ssdecode.py 需要解析的ss链接
```
输出json格式的配置和转换成ssr配置的链接，方便直接从ssr客户端导入。
# 其他说明
现阶段支持解析由安卓ss客户端导出的配置链接格式，如这种
```
ss://YWVzLTI1Ni1jZmI6YjQ3MTk1NDZkMGJkOWNjNjMzZWNiMTc0ZmY3NWYyYjA@140.207.47.98:29610
```
**暂时不支持带obfs参数的ss链接**。

