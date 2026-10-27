
Develop a simple ETL pipeline using a language like Python or SQL. The pipeline must first Extract data from a provided CSV file. Then, clean and Transform the data by implementing at least two rules (e.g., removing nulls in a key column or formatting dates). Finally, Load the cleaned data into a new table or a new output file. Display the loaded data and briefly explain the purpose of each ETL step.
  

Third Exp

Run: mysql -u root -p
Next: 

-- 1. CREATE SOURCE DATABASE
CREATE DATABASE IF NOT EXISTS retail_source;
USE retail_source;

-- 2. CREATE SOURCE TABLE
CREATE TABLE sales_transaction (
    Transaction_ID INT PRIMARY KEY,
    Date DATE,
    Customer_ID INT,
    Gender VARCHAR(10),
    Age INT,
    Product_Category VARCHAR(50),
    Quantity INT,
    Price_per_Unit DECIMAL(10,2),
    Total_Amount DECIMAL(10,2)
);

-- 3. INSERT SAMPLE DATA
INSERT INTO sales_transaction VALUES
(1,'2025-01-01',101,'Male',27,'Electronics',2,500,1000),
(2,'2025-01-02',102,'Female',30,'Grocery',5,50,250),
(3,'2025-01-02',103,'Male',40,'Clothing',3,200,600),
(4,'2025-01-03',104,'Female',22,'Furniture',1,800,800),
(5,'2025-01-03',105,'Male',35,'Clothing',4,150,600),
(6,'2025-01-04',106,'Female',28,'Electronics',1,700,700),
(7,'2025-01-04',107,'Male',42,'Grocery',10,40,400),
(8,'2025-01-05',108,'Female',33,'Furniture',2,1200,2400),
(9,'2025-01-05',109,'Male',27,'Beauty',5,100,500),
(10,'2025-01-06',110,'Female',38,'Electronics',1,900,900),
(11,'2025-01-07',111,'Male',29,'Furniture',1,1500,1500),
(12,'2025-01-07',112,'Female',24,'Beauty',3,100,300),
(13,'2025-01-08',113,'Male',31,'Beauty',2,200,400),
(14,'2025-01-08',114,'Female',41,'Electronics',2,850,1700),
(15,'2025-01-09',115,'Male',37,'Grocery',8,60,480),
(16,'2025-01-09',116,'Female',32,'Clothing',3,250,750),
(17,'2025-01-10',117,'Male',45,'Electronics',1,1000,1000),
(18,'2025-01-10',118,'Female',29,'Furniture',1,900,900),
(19,'2025-01-11',119,'Male',34,'Grocery',5,55,275),
(20,'2025-01-12',120,'Female',26,'Clothing',2,200,400);

-- 4. CREATE DATA WAREHOUSE
CREATE DATABASE IF NOT EXISTS retail_dw;
USE retail_dw;

-- 5. CREATE CUSTOMER DIMENSION
CREATE TABLE dim_customer (
    Customer_ID INT PRIMARY KEY,
    Gender VARCHAR(10),
    Age INT
);

-- 6. CREATE PRODUCT DIMENSION
CREATE TABLE dim_product (
    Product_ID INT AUTO_INCREMENT PRIMARY KEY,
    Product_Category VARCHAR(50) UNIQUE
);

-- 7. CREATE TIME DIMENSION
CREATE TABLE dim_time (
    Date DATE PRIMARY KEY,
    Year INT,
    Month INT,
    Day INT
);

-- 8. CREATE FACT TABLE
CREATE TABLE fact_sales (
    Transaction_ID INT PRIMARY KEY,
    Date DATE,
    Customer_ID INT,
    Product_ID INT,
    Quantity INT,
    Total_Amount DECIMAL(10,2),
    FOREIGN KEY (Customer_ID)
        REFERENCES dim_customer(Customer_ID),
    FOREIGN KEY (Product_ID)
        REFERENCES dim_product(Product_ID),
    FOREIGN KEY (Date)
        REFERENCES dim_time(Date)
);

-- 9. EXTRACT DATA INTO STAGING TABLE
CREATE TABLE staging_sales AS
SELECT * FROM retail_source.sales_transaction;

-- 10. TRANSFORM DATA
DELETE FROM staging_sales
WHERE Total_Amount IS NULL
   OR Quantity IS NULL
   OR Quantity <= 0;

UPDATE staging_sales
SET Total_Amount = Quantity * Price_per_Unit
WHERE Total_Amount <> Quantity * Price_per_Unit;

-- 11. LOAD CUSTOMER DIMENSION
INSERT INTO dim_customer (Customer_ID, Gender, Age)
SELECT DISTINCT Customer_ID, Gender, Age
FROM staging_sales;

-- 12. LOAD PRODUCT DIMENSION
INSERT INTO dim_product (Product_Category)
SELECT DISTINCT Product_Category
FROM staging_sales;

-- 13. LOAD TIME DIMENSION
INSERT INTO dim_time (Date, Year, Month, Day)
SELECT DISTINCT Date, YEAR(Date), MONTH(Date), DAY(Date)
FROM staging_sales;

-- 14. LOAD FACT TABLE
INSERT INTO fact_sales
    (Transaction_ID, Date, Customer_ID,
     Product_ID, Quantity, Total_Amount)
SELECT s.Transaction_ID, s.Date, s.Customer_ID,
       p.Product_ID, s.Quantity, s.Total_Amount
FROM staging_sales s
JOIN dim_product p
    ON s.Product_Category = p.Product_Category;

-- 15. ANALYSIS 1: TOTAL SALES BY PRODUCT CATEGORY
SELECT p.Product_Category,
       SUM(f.Total_Amount) AS Total_Sales
FROM fact_sales f
JOIN dim_product p ON f.Product_ID = p.Product_ID
GROUP BY p.Product_Category
ORDER BY Total_Sales DESC;

-- 16. ANALYSIS 2: AVERAGE SPENDING BY GENDER
SELECT c.Gender,
       AVG(f.Total_Amount) AS Avg_Spending
FROM fact_sales f
JOIN dim_customer c ON f.Customer_ID = c.Customer_ID
GROUP BY c.Gender;

-- 17. ANALYSIS 3: MONTHLY SALES TREND
SELECT t.Year, t.Month,
       SUM(f.Total_Amount) AS Monthly_Sales
FROM fact_sales f
JOIN dim_time t ON f.Date = t.Date
GROUP BY t.Year, t.Month
ORDER BY t.Year, t.Month;

-- 18. ANALYSIS 4: TOP 5 CUSTOMERS BY TOTAL SPENDING
SELECT c.Customer_ID,
       SUM(f.Total_Amount) AS Total_Spending
FROM fact_sales f
JOIN dim_customer c ON f.Customer_ID = c.Customer_ID
GROUP BY c.Customer_ID
ORDER BY Total_Spending DESC
LIMIT 5;

-- 19. VERIFY TOTAL TRANSACTIONS
SELECT COUNT(*) AS Total_Transactions
FROM fact_sales;
