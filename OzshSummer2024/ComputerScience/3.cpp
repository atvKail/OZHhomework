#include <iostream>
#include <unordered_map>
#include <vector>
#include <string>
#include <algorithm>

using namespace std;

int main() {
    int N;
    cin >> N;
    cin.ignore();

    unordered_map<string, int> school_counts;

    for (int i = 0; i < N; ++i) {
        string surname, initials, school_number;
        cin >> surname >> initials >> school_number;
        ++school_counts[school_number];
    }

    int max_count = 0;
    for (const auto& pair : school_counts) {
        if (pair.second > max_count) {
            max_count = pair.second;
        }
    }

    vector<string> schools_with_max_participants;
    for (const auto& pair : school_counts) {
        if (pair.second == max_count) {
            schools_with_max_participants.push_back(pair.first);
        }
    }

    sort(schools_with_max_participants.begin(), schools_with_max_participants.end());

    for (const string& school : schools_with_max_participants) {
        cout << school << endl;
    }

    return 0;
}