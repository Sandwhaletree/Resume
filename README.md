# Python作品集

* [財經]快速查詢上市、上櫃、興櫃與公發公司之財務報表 [(Gooogle Colab)](https://colab.research.google.com/drive/1ESoexBqL4ErdWrC9mfO7pykyIBeG2Fcx#scrollTo=2PEirgokFqXz)
  * 痛點: 製作同業比較常需挑選產業3-5位競爭者作為產業代表，然而數據撈取需分別下載年報、手動key上數據，易費時也較容易出錯
  * 設計: 透過爬蟲撈取政府公開之API資料，透過表格清洗與整理，將表格格式化整合並產出
  * 貢獻: 能一次性撈取同市場別之財務報表
  
* [財經]快速查詢公司代碼&公司資訊 [(Gooogle Colab)](https://colab.research.google.com/drive/1ClTGgG5oYzMiSGH4zDOv3igBCjJlzDt4#scrollTo=-m2Ty-UBEiPJ)
  * 痛點: 開發新上市櫃客戶，需快速查詢整批公司代碼了解公司本身、競爭者、上下游供應商等公司資訊，查詢資訊時易浪費時間
  * 設計: 透過爬蟲撈取政府公開之API資料，透過表格整理與遍歷清單，找出對應之公司代碼相關簡易資訊
  * 貢獻: 能整批撈取公司基本資訊
  
* [財經]經濟部商業司-公司名稱&統一編號整批快速查詢 [(Gooogle Colab)](https://colab.research.google.com/drive/1D8eIfSF8jw3sUNYKme2cIq97OWquL7gV#scrollTo=rIBR9VATT5d2)
  * 痛點: 財務人員只要做交易或寫報告，皆需查詢公司之經濟部商業司確保公司資訊為最新，然而查詢5家以上整批資訊時易浪費時間
  * 設計: 透過爬蟲撈取政府公開之API資料，透過表格整理、清洗與遍歷清單，找出對應之公司名稱與經濟部商業司資訊
  * 貢獻: 能整批撈取即時公司經濟部商業司資訊

* [財經]公開資訊站_自動下載年報PDF(完整版) [(Gooogle Colab)](https://colab.research.google.com/drive/1vobYJVERg5rEQNu9WPhw0hLmwtDlRsVO#scrollTo=zEufFHJcsH3v)
  * 設計: 透過selenium自動化，快速下載上市櫃公司年報

* [求職]104職缺_市場調查 [(Gooogle Colab)](https://colab.research.google.com/drive/1fRuNujDFXbNJicpSj3Ng_9FC5RZ8qfwM#scrollTo=Adsu_BPSTGAs)
  * 設計: 透過requests與bs4爬蟲，撈取104網站共50頁(1000筆資料)想要的職缺名稱相關求職資訊(地址、薪資、網站連結)

* [求職]104&1111求職爬蟲 [(Gooogle Colab)](https://colab.research.google.com/drive/1dT5jOhUYA_RURXs2RaRW5hQK94mHWmEA)
  * 設計: 透過selenium自動化與爬蟲，即時下載想要的特定職缺數據，並用pandas做簡單的分析

* [求職]104工作薪資情報-整批圖片下載 [(Jupyter)](https://github.com/Sandwhaletree/Resume/blob/main/104%E5%B7%A5%E4%BD%9C%E8%96%AA%E8%B3%87%E6%83%85%E5%A0%B1-%E6%95%B4%E6%89%B9%E5%9C%96%E7%89%87%E4%B8%8B%E8%BC%89_230824_final_opt.ipynb)
  * 設計: 透過selenium自動化與爬蟲，快速蒐集工作職缺薪資情報

* [求職]求職文字雲 [(Gooogle Colab)](https://colab.research.google.com/drive/1mOR1tb_xApIYbYXUW_hi9RA0cgMxlo4P#scrollTo=G3cjyZiUj9Y0)
  * 設計: 透過wordcloud文字雲與蒐集之文字數據，以plt方式呈現量化後之數據圖表
 <br/><img src="https://github.com/Sandwhaletree/Resume/blob/5835283982c22158e97106ad134a1278a0bf6ea2/2023-04-20_%E6%B1%82%E8%81%B7%E6%96%87%E5%AD%97%E9%9B%B2.png" width="300" >
