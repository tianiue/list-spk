# OpenList 群晖客户端-暂时不可用

OpenList群晖客户端是一个专为群晖NAS设计的应用程序，用于连接OpenList网盘服务，将远程存储映射为本地文件夹。

## 功能特点

- 支持OpenList API和WebDAV两种连接方式
- 将OpenList网盘内容映射为群晖本地共享文件夹
- 支持文件的读写、删除、移动等操作
- 集成群晖DSM系统，支持开机自动挂载
- 简洁直观的用户界面

## 安装方法

1. 下载最新的SPK安装包
2. 打开群晖DSM的"套件中心"
3. 点击右上角的"手动安装"
4. 选择下载的SPK文件，按照提示完成安装

## 使用说明

1. 安装完成后，在群晖桌面找到并启动OpenList客户端
2. 在"连接设置"标签页：
   - 选择连接方式（WebDAV或API）
   - 输入OpenList服务器地址
   - 输入用户名和密码
   - 点击"连接"按钮
3. 在"挂载设置"标签页：
   - 确认或修改本地挂载目录
   - 点击"挂载"按钮
4. 完成后，即可通过群晖文件管理器访问`/volume1/OpenList_Mount`目录操作远程文件

## 卸载方法

1. 打开群晖DSM的"套件中心"
2. 在"已安装"列表中找到"OpenList客户端"
3. 点击"卸载"并按照提示操作

## 构建方法

如果需要自行构建SPK包：
# 克隆仓库
git clone https://github.com/tianiue/olist-spk.git   
cd olist-spk

# 构建SPK
mkdir -p build/target
cp -r src/* build/target/
cp -r package/* build/
cd build
tar --format=gnu -cvf ../openlist-synology-1.0.0.spk *
## 许可证

MIT
