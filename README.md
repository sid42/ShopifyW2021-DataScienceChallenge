Question 1

a. The naive solution is calculating the average over the 'order_amounts' column ($3145.128). While this a reasonable estimate
   of the average amount of the orders made at each store, it is not indicative of the average shoe price as it does not take into 
   account the number of shoes being sold, thus giving us an estimate higher than the expected value of a single shoe. 
   
b. A better way to calculate the average shoe price would be to calculate the price of the individual shoe sold at each store by 
   dividing the total amount of the order placed by the number of units at each store sold and then calculate the average of this value 
   over all the stores.  

c. The new Average Order Value computes to $387.74.


Question 2

a. 
SELECT COUNT(*) 
FROM [Orders] 
WHERE ShipperID = 1

Answer = 54

b. 
SELECT LastName FROM Employees
INNER JOIN (SELECT EmployeeID, COUNT(*) as UnitsSold 
			FROM [Orders] 
            GROUP BY EmployeeID 
            ORDER BY UnitsSold DESC 
            LIMIT 1
            ) as EmpSold
ON
Employees.EmployeeID = EmpSold.EmployeeID

Answer = Peacock

c. 
SELECT ProductName FROM [Products]
INNER JOIN (SELECT ProductID, SUM(Quantity) as Quantity 
            FROM OrderDetails 
            INNER JOIN (SELECT Orders.OrderID FROM [Orders]
                        INNER JOIN (SELECT CustomerID FROM Customers 
                                    WHERE Country = 'Germany'
                                    ) as CustomersFromGermany
                        ON 
                        Orders.CustomerID = CustomersFromGermany.CustomerID 
                        ) as OrdersFromGermany
            ON 
            OrderDetails.OrderID = OrdersFromGermany.OrderID
            GROUP BY ProductID
            ORDER BY Quantity DESC 
            LIMIT 1
            ) as MostOrderedProductFromGermany
ON 
Products.ProductID = MostOrderedProductFromGermany.ProductID

Answer = Boston Crab Meat