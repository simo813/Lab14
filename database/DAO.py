from database.DB_connect import DBConnect


class DAO():
    @staticmethod
    def getStores():
        result = []
        try:
            conn = DBConnect.get_connection()
            cursor = conn.cursor(dictionary=True)
            query = """ 
                   select s.store_name, s.store_id
                   from bike_store_full.stores s 
               """
            cursor.execute(query)

            for row in cursor:
                result.append((row["store_name"], row["store_id"]))

        except Exception as e:
            print(f"Error fetching colors: {e}")
        finally:
            if cursor:
                cursor.close()
            if conn:
                conn.close()
        return result

    @staticmethod
    def getNodes(storeId):
        result = []
        try:
            conn = DBConnect.get_connection()
            cursor = conn.cursor(dictionary=True)
            query = """ 
                          select o.order_id 
                          from bike_store_full.orders o
                          where o.store_id = %s
                       """
            cursor.execute(query, (int(storeId),))

            for row in cursor:
                result.append(row["order_id"])

        except Exception as e:
            print(f"Error fetching colors: {e}")
        finally:
            if cursor:
                cursor.close()
            if conn:
                conn.close()
        return result

    @staticmethod
    def getEdge(node1, node2, maxDays):
        result = []
        try:
            conn = DBConnect.get_connection()
            cursor = conn.cursor(dictionary=True)
            query = """ 
                              select o.order_id, o2.order_id, sum(oi.quantity + oi2.quantity)
                                from bike_store_full.orders o, bike_store_full.order_items oi , bike_store_full.orders o2, bike_store_full.order_items oi2
                                where 		o.store_id = 1 
                                        and o.order_id = oi.order_id
                                        and o2.order_id = oi2.order_id
                                        and o.store_id = o2.store_id
                                        and datediff(o.order_date, o2.order_date) < 5
                                        and o.order_date > o2.order_date
                                group by o.order_id, o2.order_id 

                           """
            cursor.execute(query, (int(storeId),))

            for row in cursor:
                result.append(row["order_id"])

        except Exception as e:
            print(f"Error fetching colors: {e}")
        finally:
            if cursor:
                cursor.close()
            if conn:
                conn.close()
        return result

