Design a small data warehouse structure consisting of two dimension tables (Customer and Product) and one fact table (Sales). Insert sufficient sample data into these tables, ensuring all foreign key relationships are valid. Using SQL, write and execute queries to calculate the total sales by product category and the total sales by customer region. Finally, display the results and explain how warehousing improves data analysis compared to querying raw transactional tables.


sql
Second Exp

Run: mysql -u root -p
Next: --STAR SCHEMA FOR RETAIL SALES DATA WAREHOUSE

-- 1. Create Database
CREATE DATABASE IF NOT EXISTS retail_dw;
USE retail_dw;

-- 2. Create Customer Dimension
CREATE TABLE dim_customer (
    customer_id INT PRIMARY KEY,
    gender VARCHAR(10),
    age INT
);

-- 3. Create Product Dimension
CREATE TABLE dim_product (
    product_category VARCHAR(50) PRIMARY KEY
);

-- 4. Create Time Dimension
CREATE TABLE dim_time (
    date_key DATE PRIMARY KEY,
    year INT,
    month INT,
    day INT
);

-- 5. Create Fact Table
CREATE TABLE fact_sales (
    transaction_id INT PRIMARY KEY,
    customer_id INT,
    product_category VARCHAR(50),
    date_key DATE,
    quantity INT,
    total_amount DECIMAL(10,2),
    FOREIGN KEY (customer_id) REFERENCES dim_customer(customer_id),
    FOREIGN KEY (product_category) REFERENCES dim_product(product_category),
    FOREIGN KEY (date_key) REFERENCES dim_time(date_key)
);

-- 6. Insert Customer Data
INSERT INTO dim_customer VALUES
(101,'Male',25),
(102,'Female',30),
(103,'Male',40),
(104,'Female',22);

-- 7. Insert Product Data
INSERT INTO dim_product VALUES
('Electronics'),
('Clothing'),
('Grocery');

-- 8. Insert Time Data
INSERT INTO dim_time VALUES
('2025-01-01',2025,1,1),
('2025-01-02',2025,1,2),
('2025-01-03',2025,1,3);

-- 9. Insert Sales Data
INSERT INTO fact_sales VALUES
(1,101,'Electronics','2025-01-01',2,1000.00),
(2,102,'Clothing','2025-01-02',3,600.00),
(3,103,'Electronics','2025-01-02',1,500.00),
(4,104,'Grocery','2025-01-03',5,250.00);

-- 10. ANALYSIS 1: Total Sales by Product Category
SELECT
    product_category,
    SUM(total_amount) AS total_sales
FROM fact_sales
GROUP BY product_category
ORDER BY total_sales DESC;

-- 11. ANALYSIS 2: Total Sales by Gender
SELECT
    c.gender,
    SUM(f.total_amount) AS total_sales
FROM fact_sales f
JOIN dim_customer c
    ON f.customer_id = c.customer_id
GROUP BY c.gender
ORDER BY total_sales DESC;

-- 12. ANALYSIS 3: Monthly Sales Trend
SELECT
    YEAR(date_key) AS year,
    MONTH(date_key) AS month,
    SUM(total_amount) AS monthly_sales
FROM fact_sales
GROUP BY YEAR(date_key), MONTH(date_key)
ORDER BY year, month;
