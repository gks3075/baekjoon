# 최댓값
m_id = 0
m_val = 0
for i in range(9):
    a = int(input())
    if m_val < a:
        m_val = a
        m_id = i + 1

print(m_val)
print(m_id)