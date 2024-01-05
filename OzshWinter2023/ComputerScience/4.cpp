#include <fstream>
#include <vector>
#include <cmath>
#include <iostream>
using namespace std;

struct point {
    double x = 0, y = 0;
};


ifstream in;
ofstream out;
double vx, vy, gx, gy, xc, yc;
int t = 0, n = 0;
vector<point> p;

bool PointInPoly(){
    bool result = false;
    int j = n - 1;
    for (int i = 0; i < n; i++) {
        if ( (p[i].y < gy && p[j].y >= gy || p[j].y < gy && p[i].y >= gy) &&
            (p[i].x + (gy - p[i].y) / (p[j].y - p[i].y) * (p[j].x - p[i].x) < gx) )
            result = !result;
        j = i;
    }
    return result;
}

int main() {
    in.open("INPUT.txt");
    out.open("OUTPUT.txt");
    in >> n;
    for (int i = 0; i < n; i++) {
        double x, y;
        in >> x >> y;
        point po;
        po.x = x; po.y = y;
        p.push_back(po);
        xc += x;
        yc += y;
    }
    xc /= n;
    yc /= n;
    in >> vx >> vy >> gx >> gy;
    double prev = sqrt(pow(gx - xc, 2)+ pow(gy - yc, 2));
    bool res = PointInPoly();
    while (prev >= sqrt(pow(gx - xc, 2)+ pow(gy - yc, 2)) && !res) {
        t++;
        gx -= vx;
        gy -= vy;
        res = PointInPoly();
        prev = sqrt(pow(gx - xc, 2)+ pow(gy - yc, 2));
    }
    if (t == 0 && res){
        out << "Огород под облаком" << endl;
    }
    else if (t > 12 && res){
        out << "Облако не дойдет до огорода за 12 часов" << endl;
    }
    else if (res){
        out << t << endl;   // В тестовых 4 4 -> 1 ;  Мне кажется, что должно быть два, т.к. дана скорость в часах 1 час (3, 3) 2 час (2, 2)
    }
    else{
        out << "Облако не заденет огорода" << endl;
    }
    return 0;
}
