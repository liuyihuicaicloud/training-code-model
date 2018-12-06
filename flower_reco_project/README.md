flower_reco_project 上传至个人存储根目录，可按如下步骤运行 demo

### 打标
### notebook
1. 训练代码目录 flower_reco_project/code/flower_train.py
2. 参数意义及默认值请见代码
### 训练
1. 训练脚本 flower_reco_project/code/flower_train.py
2. 必填参数为 --model_version=xxx，xxx 为一不重复的版本标记
3. 其他选填参数请见代码
4. 代码支持 GPU，已知配额 1GB 内存时会 OOM，4GB 时 OK，边界值待试
5. 默认输出模型目录为 flower_reco_project/output/models/xxx，默认输出 events 目录为 flower_reco_project/output/events/xxx
### 可视化
1. 略，目录可选至  flower_reco_project/output/events
### 发布服务
1. 模型配置选至 savedmodel.pb 所在目录
2. 略
### 访问服务
1. python + gRPC 环境直接运行 client 代码
2. 10.130.1.201:30000 应用中已有应用 serving-demo，服务 clever-serving-demo 访问地址可上传图片验证
3. 10.130.1.201:30000 中已有应用模版 serving-demo，完整 demo 演示流程应该为通过应用模版新建 client 应用，再演示 client 访问
