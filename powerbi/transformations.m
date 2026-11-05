// Paste into Power Query Advanced Editor, update file path to fact_sales.csv.
let
    Source = Csv.Document(File.Contents("C:\\REPLACE_WITH_PROJECT_PATH\\data\\fact_sales.csv"), [Delimiter=",", Encoding=65001, QuoteStyle=QuoteStyle.Csv]),
    Promoted = Table.PromoteHeaders(Source, [PromoteAllScalars=true]),
    Typed = Table.TransformColumnTypes(Promoted, {{"line_id", type text}, {"order_id", type text}, {"order_date", type date}, {"customer_id", type text}, {"product_id", type text}, {"quantity", Int64.Type}, {"unit_price", type number}, {"discount", type number}, {"sales", Currency.Type}, {"cost", Currency.Type}, {"profit", Currency.Type}}),
    Clean = Table.TransformColumns(Typed, {{"order_id", Text.Trim, type text}, {"customer_id", Text.Trim, type text}, {"product_id", Text.Trim, type text}}),
    Valid = Table.SelectRows(Clean, each [quantity] > 0 and [sales] >= 0 and [cost] >= 0)
in
    Valid
