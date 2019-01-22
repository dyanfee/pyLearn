# Scrapy

## 爬虫框架
- scrapy
- pysprder
- crawley

## Scrapy学习
- [英文文档](https://docs.scrapy.org/en/latest/)
- [中文文档](https://scrapy-chs.readthedocs.io/zh_CN/latest/) 

## Scrapy 构架
- 部件
    - ScrapyEngine
    - Schedler
    - Downloader
    - Spider
    - ItemPipeline
    - DownloaderMiddleware
    - SpiderMiddleware
- 流程
    - 建项目 scrapy startproject xx
    - item.py
    - url
    - save pipeline.py
- ItemPipeline
    - 数据进一步处理 处理 process-item函数
    - process_item
        - spider 传入item spider
         - 核心 必须返回Item
    - __init\__: 构造函数
    - open_spider(spider)
    - close_spider(spider)
- Spider 
    - spiders目录下
    - __init\__
    - start_requests
    - parse
    - start_request
    - name
    - start_urls
    - allow_domains
    - log
- DownloaderMiddleware
    - 