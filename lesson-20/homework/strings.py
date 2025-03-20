#TASK 1
import sqlite3
import pandas as pd

# Connect to the SQLite database
conn = sqlite3.connect('chinook.db')

# Customer Purchases Analysis: Top 5 Customers
customer_purchases_query = """
SELECT c.CustomerId, c.FirstName || ' ' || c.LastName AS CustomerName, SUM(i.Total) AS TotalSpent
FROM customers c
JOIN invoices i ON c.CustomerId = i.CustomerId
GROUP BY c.CustomerId
ORDER BY TotalSpent DESC
LIMIT 5;
"""
top_customers = pd.read_sql(customer_purchases_query, conn)
print("Top 5 Customers by Total Spent:\n", top_customers)

#TASK 2

# Album vs. Individual Track Purchases Analysis
album_vs_tracks_query = """
WITH InvoiceAlbumTracks AS (
    SELECT il.InvoiceId, t.AlbumId, COUNT(DISTINCT il.TrackId) AS PurchasedTracksCount, 
           (SELECT COUNT(TrackId) FROM tracks WHERE AlbumId = t.AlbumId) AS TotalTracksCount
    FROM invoice_items il
    JOIN tracks t ON il.TrackId = t.TrackId
    GROUP BY il.InvoiceId, t.AlbumId
),
CustomerPreference AS (
    SELECT i.CustomerId,
           CASE 
               WHEN SUM(CASE WHEN PurchasedTracksCount < TotalTracksCount THEN 1 ELSE 0 END) > 0 THEN 'Individual Tracks'
               ELSE 'Full Albums'
           END AS PurchasePreference
    FROM InvoiceAlbumTracks iat
    JOIN invoices i ON i.InvoiceId = iat.InvoiceId
    GROUP BY i.CustomerId
)
SELECT PurchasePreference, COUNT(*) * 100.0 / (SELECT COUNT(*) FROM customers) AS Percentage
FROM CustomerPreference
GROUP BY PurchasePreference;
"""

customer_preferences = pd.read_sql(album_vs_tracks_query, conn)
print("\nCustomer Purchase Preferences:\n", customer_preferences)

# Close the database connection
conn.close()
