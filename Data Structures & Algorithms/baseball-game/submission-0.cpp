class Solution {
public:
    int calPoints(vector<string>& operations) {
        vector<int> record; // This acts as our stack

        for (const string& op : operations) {
            if (op == "+") {
                // Add the sum of the last two scores
                int top1 = record.back();
                int top2 = record[record.size() - 2];
                record.push_back(top1 + top2);
            } 
            else if (op == "D") {
                // Double the last score
                record.push_back(2 * record.back());
            } 
            else if (op == "C") {
                // Invalidate/remove the last score
                record.pop_back();
            } 
            else {
                // It's an integer string, convert and record it
                record.push_back(stoi(op));
            }
        }

        // Finally, calculate the total sum of all scores left in the record
        int totalSum = 0;
        for (int score : record) {
            totalSum += score;
        }

        return totalSum;
    }
};