{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 1,
   "id": "b13abcbb",
   "metadata": {},
   "outputs": [],
   "source": [
    "!pip install -q streamlit "
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 4,
   "id": "de5d1465",
   "metadata": {},
   "outputs": [
    {
     "name": "stderr",
     "output_type": "stream",
     "text": [
      "2022-07-24 19:15:42.188 INFO    numexpr.utils: NumExpr defaulting to 8 threads.\n"
     ]
    }
   ],
   "source": [
    "import streamlit as st "
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 5,
   "id": "b3b36e3d",
   "metadata": {},
   "outputs": [
    {
     "name": "stderr",
     "output_type": "stream",
     "text": [
      "2022-07-24 19:15:46.699 \n",
      "  \u001b[33m\u001b[1mWarning:\u001b[0m to view this Streamlit app on a browser, run it with the following\n",
      "  command:\n",
      "\n",
      "    streamlit run C:\\Users\\DELL\\anaconda3\\lib\\site-packages\\ipykernel_launcher.py [ARGUMENTS]\n"
     ]
    },
    {
     "data": {
      "text/plain": [
       "DeltaGenerator(_root_container=0, _provided_cursor=None, _parent=None, _block_type=None, _form_data=None)"
      ]
     },
     "execution_count": 5,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "st.header(\"Greatest of three number\")"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 6,
   "id": "50c90332",
   "metadata": {},
   "outputs": [],
   "source": [
    "number_1 = st.number_input(\"Number one \")"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 7,
   "id": "1ab51d63",
   "metadata": {},
   "outputs": [],
   "source": [
    "number_2 = st.number_input(\"Number two \")"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 8,
   "id": "38b0a6fd",
   "metadata": {},
   "outputs": [],
   "source": [
    "number_3 = st.number_input(\"Number three \")"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 9,
   "id": "9cd15168",
   "metadata": {},
   "outputs": [],
   "source": [
    "data = {\"number1\": number_1, \"number2\": number_2 , \"number3\": number_3}"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 10,
   "id": "b3a3cfaa",
   "metadata": {},
   "outputs": [],
   "source": [
    "c = 0\n",
    "for i in data.keys():\n",
    "    if data[i] > c: \n",
    "        c = data[i]"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 11,
   "id": "0a98858a",
   "metadata": {},
   "outputs": [],
   "source": [
    "st.write(c)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "4b4758a5",
   "metadata": {},
   "outputs": [],
   "source": []
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3 (ipykernel)",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.9.12"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}
