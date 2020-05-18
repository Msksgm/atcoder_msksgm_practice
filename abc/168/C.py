import numpy as np


def main():
    a, b, h, m = map(int, input().split())
    short_needle = np.array([a*np.cos(np.radians(-h*30-30*((m*6)/360)+90)), a*np.sin(np.radians(-h*30-30*((m*6)/360)+90))])
    long_needle = np.array([b*np.cos(np.radians(-m*6+90)), b*np.sin(np.radians(-m*6+90))])
    ans = np.linalg.norm(short_needle - long_needle)
    print(ans)


if __name__ == "__main__":
    main()
