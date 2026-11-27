class Solution:
    def calPoints(self, operations: List[str]) -> int:
        records = []
        for op in operations:
            len_rec = len(records)
            if op == "C":
                if records : 
                    records.pop()
            elif op == "+":
                if records : 
                    sum_rec = records[len_rec-1]+records[len_rec-2]
                    records.append(sum_rec)
            elif op == "D":
                if records :
                    double_rec = 2*records[len_rec-1]
                    records.append(double_rec)
            else:
                int_record = int(op)
                records.append(int_record)
        
        return sum(records)
                
