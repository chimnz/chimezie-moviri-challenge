SELECT e.EmployeeId staff_member, SUM(items.UnitPrice * items.Quantity) total_invoice_sum
	FROM employees e
	LEFT JOIN customers c
	ON e.EmployeeId = c.SupportRepId
	LEFT JOIN invoices i
	ON i.CustomerId = c.CustomerId
	LEFT JOIN invoice_items items
	ON items.InvoiceId = i.InvoiceId
	GROUP BY staff_member
	ORDER BY total_invoice_sum DESC;