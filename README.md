# Sandy Fan's 作品集

* [財經]快速查詢上市、上櫃、興櫃與公發公司之財務報表 [(Gooogle Colab)](https://colab.research.google.com/drive/1ESoexBqL4ErdWrC9mfO7pykyIBeG2Fcx#scrollTo=2PEirgokFqXz)
  * 痛點: 財務人員在製作同業比較時，需要以同產業3-5個競爭者作為產業代表，並撈取其財務報表作為獲益比較，然而每家公司需要分別去下載年報，並分別手動key上財報數據，易費時也較容易出錯
  * 設計: 透過爬蟲撈取政府公開之API資料，透過表格清洗與整理，將表格格式化整合並產出
  * 貢獻: 能一次性撈取同市場別之財務報表
  * 改善空間: 1)可依照產業別，將範圍縮小至同產業之競爭公司 2)輸入公司代碼，可直接產出同產業之競爭公司
  
* [財經]快速查詢公司代碼&公司資訊 [(Gooogle Colab)](https://colab.research.google.com/drive/1ClTGgG5oYzMiSGH4zDOv3igBCjJlzDt4#scrollTo=-m2Ty-UBEiPJ)
  * 痛點: 財務人員若要開發新上市櫃客戶，會需要快速查詢整批公司代碼了解公司本身、競爭者、上下游供應商等等公司資訊，查詢資訊時易浪費時間
  * 設計: 透過爬蟲撈取政府公開之API資料，透過表格整理與遍歷清單，找出對應之公司代碼相關簡易資訊
  * 貢獻: 能整批撈取公司基本資訊
