Take a real-world dataset. First, clean the data by handling any missing values or inconsistencies, then perform analysis to identify at least two significant patterns or insights relevant to the business. Finally, visualize the key findings using appropriate graphs or charts and summarize how big data analysis helps in making better business decisions.

Design a small data warehouse structure consisting of two dimension tables (Customer and Product) and one fact table (Sales). Insert sufficient sample data into these tables, ensuring all foreign key relationships are valid. Using SQL, write and execute queries to calculate the total sales by product category and the total sales by customer region. Finally, display the results and explain how warehousing improves data analysis compared to querying raw transactional tables.

Develop a simple ETL pipeline using a language like Python or SQL. The pipeline must first Extract data from a provided CSV file. Then, clean and Transform the data by implementing at least two rules (e.g., removing nulls in a key column or formatting dates). Finally, Load the cleaned data into a new table or a new output file. Display the loaded data and briefly explain the purpose of each ETL step.

Use the existing Hadoop setup to first create a directory in HDFS and upload a sample text file. Then, write and execute a MapReduce program (e.g., in Java or Python Streaming) that is designed to count how often each word appears in the uploaded text file. Once the job completes, view the output file in HDFS and describe the process by which the Mapper and Reducer components handled the data.


Create a simple Java project and add at least one external library dependency by configuring the pom.xml file. Build and run the project using standard Maven commands (e.g., mvn package and mvn exec:java). Show that the project compiles successfully and explain how Maven helps in managing libraries and standardizing project builds.

Write a Scala program to initialize and manipulate immutable lists, sets, and maps. The code must demonstrate the use of higher-order functions like map, filter, and reduce (or fold) to perform operations such as summing elements, sorting, or applying a transformation to all items. Run the program and display the results, concluding with an explanation of how Scala's functional features simplify coding.


Write a Scala program that defines an abstract class Shape with an abstract method area(). Define two concrete subclasses, Circle and Rectangle, and implement the area() method in each. Additionally, add a trait (like DisplayInfo) to these classes to show shape details. Run the program by creating instances of the subclasses, calling the methods, and displaying the output.

Using PySpark or Scala/Java, read a large dataset (like stock market data) into a DataFrame. Use Spark's built-in Window Functions to calculate a moving average of a numerical column (e.g., stock prices or a sensor reading). Show the top 10 rows of the result, including the new calculated column, and explain the key benefits of distributed computation in Spark.


Build a simple machine learning model using Spark MLlib to predict a categorical outcome like customer churn or product preference. This involves splitting the data into training and test sets and then training a suitable classification model. Display the model's accuracy or prediction output and explain how MLlib simplifies large-scale machine learning workflows.

Create a new GitHub repository and push at least 10 code files from your local machine, ensuring you make at least three distinct commits. Next, clone the repository into a new local folder. Retrieve and confirm one of the files you uploaded. Finally, display the commit history using the git log command and explain how GitHub helps in version control and collaboration.


Create a basic CI/CD pipeline using a tool like GitHub Actions or Jenkins. The pipeline must be configured to automatically trigger when new code is pushed and include sequential stages to Test (run a simple test or linter) and Deploy (a simple echo command simulating deployment) a Python or Java program. Show the successful execution log of the pipeline and explain its importance in automation and code quality.

Write a functional Dockerfile to containerize a simple web or Python application, then use the command line to build the Docker image with a unique tag and run the container locally with correct port mapping, verifying the application's successful execution. Next, push the image to a container registry (e.g., Docker Hub), and finally, write the necessary service definition file (e.g., Docker Compose or Kubernetes YAML) to deploy the container using an orchestration tool like Docker Swarm or Kubernetes. You must show proof that the application is running successfully on the cluster and is accessible externally, and explain two key advantages of using Docker in modern deployment processes.
=======================================

TModelLabQues.docx consist of 12 question 

This is my model question paper for big data laboratory last year from each question give how to do that and what tool is used  and explain the procedure in point wise, all should understand easyily
…
Big Data Laboratory – Model Question Paper Guide
This guide explains how to perform each experiment in your Big Data Laboratory model question paper, which tools to use, the step-by-step procedure, important commands or code, and what output you should expect.

The main goal is to help you understand the experiment and perform it practically, rather than simply memorize the answers.

One important point: your message contains 11 experiment descriptions, although you mentioned that the DOCX contains 12 questions. I’ll explain all 11 descriptions you provided. The missing 12th question can be added when you share it.

1. Tools required for the laboratory
File:Python logo 01.svg - Wikimedia Commons
Python

Used for data cleaning, data analysis, ETL, Spark MLlib, and simple CI/CD tests.

Apache Hadoop Logo PNG Vector (AI,  PDF,  SVG) Free Download
Hadoop and HDFS

Used to store large files and execute MapReduce jobs.

Apache Spark Architecture Explained
Apache Spark and PySpark

Used for DataFrames, window functions, distributed processing, and machine learning.

Maven Original Wordmark PNG Logo — Download Free Transparent Logo
Java, Scala, and Maven

Java is used for MapReduce and Java projects; Scala is used for functional programming and object-oriented programming; Maven manages Java project dependencies and builds.

GitHub Vs. Bitbucket: Which Code Hosting Platform is Best? - Hatica
Git and GitHub

Used for source control, commits, repositories, and collaboration.

Docker Logo Icon by Those Icons – download in PNG, SVG
Docker, GitHub Actions/Jenkins, and Kubernetes

Used for automated testing, containerization, continuous deployment, and orchestration.

Since you have already been working with Hadoop, Spark, and GitHub in your practical exercises, you can reuse those installations for the relevant questions rather than installing everything again.

Experiment 1: Data Cleaning, Analysis, and Visualization
Question: Take a real-world dataset, clean it, find business insights, and visualize the findings.

Reproducible reports with Jupyter - zerokspot.com
Tools: Python, Pandas, Matplotlib, Jupyter Notebook or VS Code.

Example dataset: Retail sales CSV file.

Procedure
Download a retail sales dataset in CSV format. You can also create a small sample dataset for practice.

Open the file using Python and Pandas.

Inspect the dataset using head(), info(), and isnull().sum().

Clean the data by removing duplicate rows, handling missing product names, and correcting invalid quantities or prices.

Calculate sales using:

Sales = Quantity × UnitPrice

Group the data by product category to calculate total sales.

Group by region or month to identify business trends.

Draw a bar chart for category sales and a line chart for monthly sales.

Write down at least two business insights.

Example Python code
import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("sales.csv")

print("Before cleaning:")
print(df.head())
print(df.isnull().sum())

df = df.drop_duplicates()
df = df.dropna(subset=["Product", "Quantity", "UnitPrice"])

df["Quantity"] = pd.to_numeric(df["Quantity"], errors="coerce")
df["UnitPrice"] = pd.to_numeric(df["UnitPrice"], errors="coerce")
df = df.dropna(subset=["Quantity", "UnitPrice"])

df = df[(df["Quantity"] > 0) & (df["UnitPrice"] >= 0)]
df["Sales"] = df["Quantity"] * df["UnitPrice"]

category_sales = df.groupby("Category")["Sales"].sum()
print(category_sales)

category_sales.plot(kind="bar", title="Sales by Category")
plt.ylabel("Total Sales")
plt.tight_layout()
plt.show()

print("Total sales:", df["Sales"].sum())

The CSV must contain the columns Product, Quantity, UnitPrice, and Category for this exact code to work.

Expected result and business insights
A category-wise sales summary.

A bar chart showing which categories generate the most revenue.

An overall sales figure.

Possible insights, based on the actual output:

The category with the highest revenue could receive more inventory or marketing investment.

A category with low revenue may need pricing changes or promotional offers.

Conclusion: Big data analysis helps businesses identify trends, reduce errors, understand customers, and make decisions based on evidence rather than guesswork.

Experiment 2: Data Warehouse Using SQL
Question: Create Customer and Product dimension tables and a Sales fact table. Insert data and calculate sales by category and region.

4 Database Schema Examples for Various Applications | Airbyte
Tools: MySQL or PostgreSQL.

Concept: Star schema.

Procedure
Open MySQL Workbench or a SQL terminal.

Create a database named SalesWarehouse.

Create two dimension tables: Customer and Product.

Create one fact table: Sales.

Set the primary keys and foreign keys correctly.

Insert sample customer and product records.

Insert sales transactions using existing customer and product IDs.

Run SQL aggregation queries and display the results.

Step 1: Create the tables
CREATE DATABASE SalesWarehouse;
USE SalesWarehouse;

CREATE TABLE Customer (
    CustomerID INT PRIMARY KEY,
    CustomerName VARCHAR(50),
    Region VARCHAR(30)
);

CREATE TABLE Product (
    ProductID INT PRIMARY KEY,
    ProductName VARCHAR(50),
    Category VARCHAR(30)
);

CREATE TABLE Sales (
    SaleID INT PRIMARY KEY,
    CustomerID INT,
    ProductID INT,
    Quantity INT,
    UnitPrice DECIMAL(10,2),
    FOREIGN KEY (CustomerID) REFERENCES Customer(CustomerID),
    FOREIGN KEY (ProductID) REFERENCES Product(ProductID)
);

Step 2: Insert sample data
INSERT INTO Customer VALUES
(1, 'Arun', 'South'),
(2, 'Priya', 'North'),
(3, 'Kumar', 'West');

INSERT INTO Product VALUES
(101, 'Laptop', 'Electronics'),
(102, 'Chair', 'Furniture'),
(103, 'Phone', 'Electronics');

INSERT INTO Sales VALUES
(1, 1, 101, 2, 40000),
(2, 2, 102, 3, 3000),
(3, 1, 103, 1, 20000),
(4, 3, 101, 1, 40000),
(5, 2, 103, 2, 20000);

Step 3: Total sales by product category
SELECT p.Category,
       SUM(s.Quantity * s.UnitPrice) AS TotalSales
FROM Sales s
JOIN Product p ON s.ProductID = p.ProductID
GROUP BY p.Category;

Expected result:

Category

TotalSales

Electronics

160000

Furniture

9000

Step 4: Total sales by customer region
SELECT c.Region,
       SUM(s.Quantity * s.UnitPrice) AS TotalSales
FROM Sales s
JOIN Customer c ON s.CustomerID = c.CustomerID
GROUP BY c.Region;

Expected result:

Region

TotalSales

South

100000

North

49000

West

40000

How does a data warehouse help?
Fact table: stores measurable business events, such as sales quantity and revenue.

Dimension tables: store descriptive information, such as customer region and product category.

Star schema: organizes information so that reporting queries can join sales facts with useful business descriptions.

Better analysis: makes it easier to compare products, regions, and time periods consistently.

A warehouse does not automatically make every query faster, but its organized structure and analytical design make reporting easier than repeatedly working with unstructured or inconsistent raw transactional data.

Experiment 3: ETL Pipeline Using Python
Question: Extract data from a CSV, clean and transform it, and load the cleaned data into a new file or table.

ETL vs ELT: Which One Should You Use and Why? - DEV Community
Tools: Python, Pandas, CSV files.

Concept: ETL = Extract, Transform, Load.

Procedure
Create a CSV file named input.csv.

Read the file using Pandas. This is the Extract step.

Remove rows with missing customer IDs and remove duplicate records.

Convert date values into a consistent date format. These are Transform steps.

Save the cleaned data as cleaned.csv. This is the Load step.

Display the resulting data to verify the pipeline.

Sample input: input.csv
CustomerID,Name,Date,Amount
1,Arun,10/01/2026,500
2,Priya,2026-01-12,800
,John,2026-01-13,300
2,Priya,2026-01-12,800
Python program: etl.py
import pandas as pd

# 1. Extract
df = pd.read_csv("input.csv")
print("Original data:")
print(df)

# 2. Transform: remove missing IDs
df = df.dropna(subset=["CustomerID"])

# Remove duplicate rows
df = df.drop_duplicates()

# Standardize date format
df["Date"] = pd.to_datetime(
    df["Date"], format="mixed", dayfirst=True,
    errors="coerce"
)

df = df.dropna(subset=["Date"])
df["Date"] = df["Date"].dt.strftime("%Y-%m-%d")

# 3. Load
df.to_csv("cleaned.csv", index=False)

print("\nCleaned and loaded data:")
print(pd.read_csv("cleaned.csv"))

Run it with:

python etl.py

Expected cleaned records:

CustomerID

Name

Date

Amount

1

Arun

2026-01-10

500

2

Priya

2026-01-12

800

Remember for the exam:

Extract — read the source data.

Transform — clean, validate, and format the data.

Load — store the processed data in its destination.

Conclusion: ETL converts raw data into clean, consistent data that is suitable for reporting and analysis.

Experiment 4: Hadoop MapReduce Word Count
Question: Upload a text file to HDFS and count the frequency of each word using MapReduce.

MapReduce教程（01）- 初识MapReduce-阿里云开发者社区
Tools: Hadoop, HDFS, Java or Python Streaming, Linux terminal.

Concept: Mapper and Reducer.

Procedure
Step 1: Check Hadoop
jps
hdfs dfs -ls /

If your Hadoop services are not running, start them using your existing Hadoop setup.

Step 2: Create a sample text file
echo "big data big analytics data" > input.txt

Step 3: Create an HDFS directory and upload the file
hdfs dfs -mkdir -p /user/hadoop/wordcount/input

hdfs dfs -put -f input.txt /user/hadoop/wordcount/input/

Verify the upload:

hdfs dfs -ls /user/hadoop/wordcount/input

Step 4: Understand the Mapper and Reducer
For this input:

big data big analytics data

The Mapper emits key-value pairs:

(big, 1)
(data, 1)
(big, 1)
(analytics, 1)
(data, 1)
After shuffle and sort, the intermediate data is grouped:

analytics -> [1]
big       -> [1, 1]
data      -> [1, 1]
The Reducer adds the values:

analytics  1
big        2
data       2
Step 5: Execute the job
If using Java, create the Mapper, Reducer, and driver classes, compile them, package them into a JAR, and execute the JAR with Hadoop. Alternatively, Python Streaming uses mapper and reducer scripts.

A Python Streaming job can be launched with:

hadoop jar "$HADOOP_HOME/share/hadoop/tools/lib/hadoop-streaming-*.jar" \
  -input /user/hadoop/wordcount/input \
  -output /user/hadoop/wordcount/output \
  -mapper "python3 mapper.py" \
  -reducer "python3 reducer.py"

This command assumes that the Python scripts are available to the Hadoop task processes and that your installation contains the Streaming JAR. On a multi-node cluster, distribute the scripts with the appropriate Streaming options. If the output directory already exists, remove it before rerunning the job.

Step 6: Display the output
hdfs dfs -cat /user/hadoop/wordcount/output/part-*

Expected output:

analytics  1
big        2
data       2
Conclusion: The Mapper converts input into intermediate key-value pairs. The shuffle and sort phase groups identical keys, and the Reducer combines their values to produce the final word counts.

Experiment 5: Java Project Using Maven
Question: Create a Java project, add an external library dependency, build it, and run it.

Maven Logo PNG Vector (SVG) Free Download
Tools: JDK, Apache Maven, VS Code or IntelliJ IDEA.

Concept: Dependency management and project building.

Procedure
Step 1: Check the installations
java -version
mvn -version

Step 2: Create a Maven project
mvn archetype:generate \
  -DgroupId=com.example \
  -DartifactId=demo \
  -DarchetypeArtifactId=maven-archetype-quickstart \
  -DinteractiveMode=false

cd demo

Step 3: Add a dependency in pom.xml
Inside the existing dependencies section, add the following external library:

<dependency>
    <groupId>org.apache.commons</groupId>
    <artifactId>commons-lang3</artifactId>
    <version>3.18.0</version>
</dependency>

Use the correct version available for your project and repository. This example uses Apache Commons Lang.

Step 4: Use the library
Edit src/main/java/com/example/App.java:

package com.example;

import org.apache.commons.lang3.StringUtils;

public class App {
    public static void main(String[] args) {
        String name = "big data laboratory";
        System.out.println(StringUtils.capitalize(name));
    }
}

Expected output:

Big data laboratory
Step 5: Build and run
mvn package

The build should report BUILD SUCCESS if compilation and tests pass.

To run with mvn exec:java, add the exec-maven-plugin to the build/plugins section of pom.xml and configure the main class as com.example.App. Then execute:

mvn exec:java

Conclusion: Maven downloads dependencies, compiles source code, runs tests, packages applications, and standardizes builds across development environments.

Experiment 6: Scala Collections and Higher-Order Functions
Question: Create immutable lists, sets, and maps and demonstrate map, filter, and reduce.

Scala Logo PNG,  Vector (AI, EPS, CDR, PDF, SVG) - iconLogoVector
Tools: Scala, Java JDK, Scala CLI or scala runner.

Concept: Immutable collections and functional programming.

Procedure
Install or check Scala.

Create a file named CollectionsDemo.scala.

Define an immutable list, set, and map.

Use map to transform elements.

Use filter to select elements.

Use reduce to calculate a total.

Run the program and inspect the output.

Program
object CollectionsDemo {
  def main(args: Array[String]): Unit = {
    val numbers = List(1, 2, 3, 4, 5)
    val unique = Set(10, 20, 20, 30)
    val prices = Map("Pen" -> 10, "Book" -> 50)

    val doubled = numbers.map(_ * 2)
    val even = numbers.filter(_ % 2 == 0)
    val sum = numbers.reduce(_ + _)

    println("List: " + numbers)
    println("Doubled: " + doubled)
    println("Even numbers: " + even)
    println("Sum: " + sum)
    println("Set: " + unique)
    println("Map: " + prices)
  }
}

Run
With Scala CLI:

scala CollectionsDemo.scala

Expected output:

List: List(1, 2, 3, 4, 5)
Doubled: List(2, 4, 6, 8, 10)
Even numbers: List(2, 4)
Sum: 15
Set: Set(10, 20, 30)
Map: Map(Pen -> 10, Book -> 50)
The order in which a set or map prints its entries may vary.

Important concepts:

List stores an ordered sequence.

Set stores unique elements.

Map stores key-value pairs.

map() transforms elements.

filter() selects elements matching a condition.

reduce() combines elements into one result.

val creates an immutable binding; immutable collections cannot be modified in place.

Conclusion: Scala's functional features allow concise data transformations without manually writing loops for every operation.

Experiment 7: Abstract Class, Inheritance, and Traits in Scala
Question: Define an abstract class Shape, implement area() in Circle and Rectangle, and use a trait to display shape information.

Tools: Scala and Scala CLI.

Procedure
Create ShapeDemo.scala.

Define an abstract class named Shape.

Declare an abstract method area().

Define a DisplayInfo trait.

Implement the abstract method in Circle and Rectangle.

Create objects and call their methods.

Display the results.

Program
trait DisplayInfo {
  def displayInfo(): Unit
}

abstract class Shape {
  def area(): Double
}

class Circle(val radius: Double)
    extends Shape with DisplayInfo {

  override def area(): Double =
    math.Pi * radius * radius

  override def displayInfo(): Unit =
    println(s"Circle radius: $radius")
}

class Rectangle(val length: Double, val width: Double)
    extends Shape with DisplayInfo {

  override def area(): Double =
    length * width

  override def displayInfo(): Unit =
    println(s"Rectangle: $length x $width")
}

object ShapeDemo {
  def main(args: Array[String]): Unit = {
    val c = new Circle(5)
    val r = new Rectangle(4, 6)

    c.displayInfo()
    println(f"Circle area: ${c.area()}%.2f")

    r.displayInfo()
    println(f"Rectangle area: ${r.area()}%.2f")
  }
}

Run
scala ShapeDemo.scala

Expected output
Circle radius: 5.0
Circle area: 78.54
Rectangle: 4.0 x 6.0
Rectangle area: 24.00
Explanation:

An abstract class defines a common structure without providing every implementation.

A subclass inherits from the abstract class and implements its abstract methods.

A trait provides reusable behavior that multiple classes can share.

override explicitly indicates that a method implements or replaces an inherited method.

Conclusion: Abstract classes and traits help organize code, promote reuse, and support polymorphism.

Experiment 8: Spark DataFrame and Window Functions
Question: Read a large dataset into Spark, calculate a moving average, and display the top 10 rows.

Learn Big Data: Master Data Engineering with Spark, SQL, AWS, and Databricks
Tools: Python, PySpark, Apache Spark, CSV dataset.

Concept: DataFrames and window functions.

Procedure
Prepare a CSV file containing stock prices or sensor readings.

Create a Spark session.

Read the CSV into a DataFrame.

Convert the date and numerical columns to suitable data types.

Define a window ordered by date.

Calculate the moving average using Spark's avg() function.

Display the first 10 rows with the new column.

Sample dataset: stock.csv
Date,Price
2026-01-01,100
2026-01-02,110
2026-01-03,120
2026-01-04,130
2026-01-05,140
PySpark program: window_avg.py
from pyspark.sql import SparkSession
from pyspark.sql.functions import avg, to_date
from pyspark.sql.window import Window

spark = SparkSession.builder \
    .appName("MovingAverage") \
    .getOrCreate()

df = spark.read.option("header", True) \
    .csv("stock.csv")

df = df.withColumn("Date", to_date("Date")) \
       .withColumn("Price", df["Price"].cast("double"))

window = Window.orderBy("Date").rowsBetween(-2, 0)

result = df.withColumn(
    "MovingAverage",
    avg("Price").over(window)
)

result.orderBy("Date").show(10, truncate=False)

spark.stop()

Run
spark-submit window_avg.py

Expected output
Date

Price

MovingAverage

2026-01-01

100

100.00

2026-01-02

110

105.00

2026-01-03

120

110.00

2026-01-04

130

120.00

2026-01-05

140

130.00

The window contains the current row and up to two preceding rows. For the first two rows, fewer than three observations are available.

Conclusion: Spark can distribute large-scale data processing across multiple executors, support parallel computation, and handle data larger than the memory of a single machine. A window function computes rolling statistics without requiring a separate manual loop for each row.

Note: this example calculates a moving average across all records. For multiple stocks or sensors, use Window.partitionBy("Symbol").orderBy("Date") so that one entity's data is not mixed with another's.

Experiment 9: Machine Learning Using Spark MLlib
Question: Train a classification model to predict customer churn or another categorical outcome.

Tools: PySpark, Spark MLlib, Python, CSV dataset.

Procedure
Prepare a dataset with customer features and a target label.

Load it into a Spark DataFrame.

Convert categorical columns to numeric features if needed.

Combine input columns into a feature vector.

Split the dataset into training and testing sets.

Train a classification algorithm, such as Logistic Regression.

Predict outcomes for the test dataset.

Calculate the model's accuracy.

Example input: customers.csv
age,monthly_spend,churn
25,500,0
45,1200,1
32,700,0
50,1500,1
28,600,0
40,1100,1
35,800,0
48,1400,1
Here, churn = 1 means the customer left, while churn = 0 means the customer stayed.

Program: churn.py
from pyspark.sql import SparkSession
from pyspark.ml.feature import VectorAssembler
from pyspark.ml.classification import LogisticRegression
from pyspark.ml.evaluation import MulticlassClassificationEvaluator

spark = SparkSession.builder \
    .appName("CustomerChurn") \
    .getOrCreate()

df = spark.read.option("header", True) \
    .option("inferSchema", True) \
    .csv("customers.csv")

assembler = VectorAssembler(
    inputCols=["age", "monthly_spend"],
    outputCol="features"
)

data = assembler.transform(df).select(
    "features",
    df["churn"].cast("double").alias("label")
)

train, test = data.randomSplit([0.8, 0.2], seed=42)

model = LogisticRegression(maxIter=20).fit(train)
predictions = model.transform(test)

predictions.select("label", "prediction", "probability").show(
    truncate=False
)

evaluator = MulticlassClassificationEvaluator(
    labelCol="label",
    predictionCol="prediction",
    metricName="accuracy"

Run
spark-submit churn.py

What output should you expect?
The program displays the actual label, predicted label, probability vector, and calculated accuracy.

The accuracy is data-dependent. With only eight illustrative records, the training and test sets may be too small for a meaningful performance estimate. Use a larger, representative dataset for a reliable business conclusion.

Conclusion: Spark MLlib integrates data preparation, model training, prediction, and evaluation into a distributed processing framework. This helps businesses analyze large customer datasets and identify customers who may be at risk of leaving.

Experiment 10: GitHub Repository and Version Control
Question: Create a repository, push at least 10 code files, make at least three commits, clone the repository, retrieve a file, and show the commit history.

Oakstone & Github | Executive Search for GTM SaaS
Tools: Git, GitHub account, terminal or VS Code.

Concept: Version control.

Procedure
Step 1: Create the repository
Open GitHub.

Sign in to your account.

Click New repository.

Enter a name such as BigData.

Create the repository.

Step 2: Create 10 code files locally
For example, create these files in a folder named BigData:

BigData/
├── experiment1.py
├── experiment2.sql
├── experiment3.py
├── mapper.py
├── reducer.py
├── App.java
├── CollectionsDemo.scala
├── ShapeDemo.scala
├── window_avg.py
└── churn.py
These are illustrative filenames. Make sure each file contains the relevant code and not just an empty placeholder.

Step 3: Initialize Git
cd BigData
git init
git branch -M main
git add .
git commit -m "Add initial laboratory programs"

Configure your Git identity first if needed:

git config --global user.name "Your Name"
git config --global user.email "you@example.com"

Use your own GitHub-associated email or your preferred privacy email.

Step 4: Make at least three distinct commits
git add experiment1.py experiment2.sql experiment3.py
git commit -m "Add data analysis and SQL experiments"

git add mapper.py reducer.py App.java
git commit -m "Add Hadoop and Maven experiments"

git add CollectionsDemo.scala ShapeDemo.scala window_avg.py churn.py
git commit -m "Add Scala and Spark experiments"

This produces three additional commits after the initial commit.

Step 5: Push to GitHub
Replace the placeholder with your actual repository URL:

git remote add origin https://github.com/YOUR_USERNAME/BigData.git
git push -u origin main

Authenticate when prompted using an appropriate GitHub-supported method. Do not put your password or access token directly in the command.

Step 6: Clone into another folder
cd ..
git clone https://github.com/YOUR_USERNAME/BigData.git BigData-clone
cd BigData-clone

Retrieve and verify a file:

cat experiment1.py

Display the commit history:

git log --oneline

Check the files:

ls

Conclusion: Git records code changes through commits, and GitHub hosts repositories so developers can share, review, and collaborate on the same project. Cloning creates another local copy of the repository and its history.

Experiment 11: CI/CD Pipeline Using GitHub Actions
Question: Automatically test a program when new code is pushed, followed by a simulated deployment.

Android GitHub Actions Setup - DEV Community
Tools: GitHub, GitHub Actions, Python.

Concept: Continuous Integration and Continuous Delivery/Deployment.

Procedure
Step 1: Create a simple Python program
Create app.py:

def add(a, b):
    return a + b

Create test_app.py:

from app import add

def test_add():
    assert add(2, 3) == 5

Step 2: Create the workflow file
Inside your repository, create:

.github/workflows/ci.yml

name: Python CI CD

on:
  push:
    branches: [main]

jobs:
  test-and-deploy:
    runs-on: ubuntu-latest

    steps:
      - name: Checkout code
        uses: actions/checkout@v4

      - name: Set up Python
        uses: actions/setup-python@v5
        with:
          python-version: "3.12"

      - name: Install test tool
        run: python -m pip install pytest

      - name: Test
        run: python -m pytest -v

      - name: Deploy simulation
        run: echo "Deployment successful"

The deployment stage here only prints a message. It does not deploy an application to a real server.

Step 3: Push the files
git add app.py test_app.py .github/workflows/ci.yml
git commit -m "Add automated CI CD pipeline"
git push origin main

Step 4: View the execution log
Open the repository on GitHub.

Select the Actions tab.

Open the workflow run triggered by the push.

Inspect the Test and Deploy simulation steps.

Expected successful log, in simplified form:

Test
1 passed

Deploy simulation
Deployment successful

Workflow completed successfully
These are expected results, not a claim that the workflow has already been executed in your repository.

Conclusion: CI/CD automates repetitive build, test, and deployment tasks. It helps detect errors earlier and makes software releases more consistent.

Experiment 12: Docker Containerization and Kubernetes Deployment
Question: Create a Docker image, run the container, push the image to Docker Hub, and deploy it using Docker Compose or Kubernetes.

Scalingo Docker Image
Develop on Kubernetes Series— Operator Dev— Coding out the Custom Resource & Reconciliation Loop | by Yashvardhan Kukreja | Medium
Tools: Docker, Docker Hub, Kubernetes (kubectl), Python Flask.

Concept: Containers and orchestration.

Procedure
Step 1: Create a simple web application
Create a folder named docker-demo.

Inside it, create app.py:

from flask import Flask

app = Flask(__name__)

@app.route("/")
def home():
    return "Big Data Lab Application Running!"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)

Create requirements.txt:

flask
Step 2: Create the Dockerfile
Create a file named Dockerfile with no file extension.

FROM python:3.12-slim

WORKDIR /app

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY app.py .

EXPOSE 5000

CMD ["python", "app.py"]

Explanation:

FROM selects the base image.

WORKDIR defines the working directory.

COPY copies application files into the image.

RUN installs the dependencies during the build.

EXPOSE documents the application's port.

CMD starts the application.

Step 3: Build and run the container
From the docker-demo directory:

docker build -t bigdata-lab:v1 .

Check the image:

docker images

Run the container:

docker run -d --name bigdata-web -p 8080:5000 bigdata-lab:v1

The port mapping means:

Host port: 8080

Container port: 5000

Test the application:

curl http://localhost:8080

Expected response:

Big Data Lab Application Running!
Step 4: Push the image to Docker Hub
Create an account at Docker Hub.

Create a repository, for example bigdata-lab.

Log in to Docker from the terminal.

Tag and push the image.

docker login

docker tag bigdata-lab:v1 YOUR_USERNAME/bigdata-lab:v1

docker push YOUR_USERNAME/bigdata-lab:v1

Replace YOUR_USERNAME with your actual Docker Hub username.

Step 5: Deploy with Kubernetes
Create a file named deployment.yaml:

apiVersion: apps/v1
kind: Deployment
metadata:
  name: bigdata-app
spec:
  replicas: 2
  selector:
    matchLabels:
      app: bigdata-app
  template:
    metadata:
      labels:
        app: bigdata-app
    spec:
      containers:
        - name: web
          image: YOUR_USERNAME/bigdata-lab:v1
          ports:
            - containerPort: 5000
---
apiVersion: v1
kind: Service
metadata:
  name: bigdata-service
spec:
  type: NodePort
  selector:
    app: bigdata-app
  ports:
    - port: 5000
      targetPort: 5000
      nodePort: 30080

Replace the image placeholder with your pushed image.

Apply the configuration:

kubectl apply -f deployment.yaml

Check the deployment:

kubectl get deployments
kubectl get pods
kubectl get services

Verify that both pods become Running and that the deployment becomes available.

For a local Kubernetes cluster, you may need to enable Kubernetes in Docker Desktop or start Minikube first. A NodePort service is typically accessible at http://NODE_IP:30080; for Minikube, use:

minikube service bigdata-service --url

Open the returned URL or test it using curl. A NodePort is not automatically accessible from the public internet; external access depends on the cluster's networking and firewall configuration.

Expected proof of success: the image is pushed to Docker Hub, the Kubernetes pods are running, the Service exists, and an HTTP request returns the application message.

Advantages of Docker
Portability: the application and its dependencies are packaged together, reducing differences between environments.

Consistency and isolation: applications run in separate containers, making deployment and dependency management easier.

Kubernetes adds orchestration capabilities such as replica management, service discovery, and recovery from certain container failures.

Final revision: Which tool should you use for each experiment?
Experiment

Main tool

Main output

1. Data analysis

Python, Pandas, Matplotlib

Insights and charts

2. Data warehouse

MySQL or PostgreSQL

SQL sales reports

3. ETL pipeline

Python, Pandas

Cleaned CSV or table

4. MapReduce

Hadoop, HDFS

Word frequency counts

5. Java and dependencies

Java, Maven

Compiled JAR and program output

6. Scala collections

Scala

List, set, and map operations

7. Scala OOP

Scala

Shape details and areas

8. Moving average

PySpark

DataFrame with rolling average

9. Machine learning

Spark MLlib

Predictions and accuracy

10. Version control

Git, GitHub

Repository and commit history

11. CI/CD

GitHub Actions or Jenkins

Automated test and deployment logs

12. Container deployment

Docker, Docker Hub, Kubernetes

Running container and deployed service
