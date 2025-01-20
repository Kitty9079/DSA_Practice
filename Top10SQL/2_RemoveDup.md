# Remove Duplicate
![alt text](image.png)

```sql
-- solution 1:
delete from cars
where model_id not in (select min(model_id)
                        from cars 
                        group by model_name,brand);

--solution 2:
delete from cars
where ctid in (
                select max(ctid)
                from cars
                group by model_name,brand
                having count(1) > 1
                );
```