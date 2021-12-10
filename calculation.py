import streamlit as st
import matplotlib.pyplot as plt

st.title('The Birthday Paradox')
st.write('Created by Jonny Linehan - @jlinehan9')

num_people = st.slider('Number of People', min_value=2, max_value=100, 
                       value=23, step=1)

probability = 1
for i in range(num_people):
    probability *= (365-i) / 365
answer = round((1-probability) * 100, 1)

prob_list = []
prob = 1
for i in range(100):
    prob *= (365-i) / 365
    prob_list.append(round((1-prob) * 100, 1))
prob = 1

fig = plt.figure()
x_range = [i for i in range(1, 101)]
plt.plot(x_range, prob_list, lw=2)
plt.title(f'Probability of a Duplicate Birthday Given {num_people} People')
plt.xlabel('Number of People')
plt.ylabel('Probability (%)')
plt.axhline(answer, lw=1, c='gray', ls='--')
plt.axvline(num_people, lw=1, c='gray', ls='--')
plt.box(on=False)
st.pyplot(fig)

st.write(f'''The probability that two (or more) people have the same birthday 
             in a group of {num_people} people is {answer}%''')
