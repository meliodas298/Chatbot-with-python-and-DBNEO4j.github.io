from neo4j import GraphDatabase
from Return_CB import *

class App:
    def __init__(self, uri, user, password):
        self.driver = GraphDatabase.driver(uri, auth=(user, password))

    def close(self):
        self.driver.close()

    def findLV(self):
        stt = 1
        elementlistsLV = []
        with self.driver.session() as session:
            result = session.read_transaction(self._find_and_return_LV)
            for row in result:
                elementlistsLV.append(return_elementLV(row, str(stt)))
                stt = stt + 1
            return elementlistsLV

    @staticmethod
    def _find_and_return_LV(tx):
        query = "Match (n:linhvuc) return n.name AS name"
        result = tx.run(query)
        return [row["name"] for row in result]

    def find_TTHC(self, LV, settthc):
        stt = 1
        elementlistsTTHC = []
        with self.driver.session() as session:
            result, Website = session.read_transaction(self._find_and_return_TTHC, LV)
            # Bot chỉ xuất tối đa 10 thành phần.
            # Vì thế nên lưu 9 thành phần đầu và 1 nút qua trang chứa các thành phần tiếp theo.
            # gán mặc định settthc = 1 khi chứa các thành phần đầu và settthc = 0 khi chứa các thành phần tiếp theo.
            for row in result:
                if settthc == 1 and stt < 10:
                    elementlistsTTHC.append(return_element_TTHC(row, str(stt), Website[stt-1]))
                elif settthc == 0 and stt == 9:
                    elementlistsTTHC.append(return_back())
                elif settthc == 0 and stt >= 10:
                    elementlistsTTHC.append(return_element_TTHC(row, str(stt), Website[stt - 1]))
                elif settthc == 1 and stt == 10:
                    elementlistsTTHC.append(return_next())
                stt = stt + 1
        return stt - 1, elementlistsTTHC

    @staticmethod
    def _find_and_return_TTHC(tx, LV):
        query1 = "match (a:linhvuc)-[r:co]->(b:TenTTHC) where a.id =$LV return b.name AS name ORDER BY b.id"
        result = tx.run(query1, LV=LV)
        query2 = "match (a:linhvuc)-[r:co]->(b:TenTTHC) where a.id =$LV return b.website AS website ORDER BY b.id"
        result1 = tx.run(query2, LV=LV)
        return [row["name"] for row in result], [row["website"] for row in result1]

    def find_ND(self, id_tthc, id_nd):
        with self.driver.session() as session:
            result = session.read_transaction(self._find_and_return_ND, id_tthc, id_nd)
            for row in result:
                kq = (" {row}".format(row=row))
            return kq

    @staticmethod
    def _find_and_return_ND(tx, id_tthc, id_nd):
        query = "match (a:TenTTHC)-[]->(b) where a.id = $id_tthc and b.id= $id_nd return b.name AS name "
        result = tx.run(query, id_tthc=id_tthc, id_nd=id_nd)
        return [row["name"] for row in result]