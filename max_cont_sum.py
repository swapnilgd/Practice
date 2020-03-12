{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 1,
   "metadata": {},
   "outputs": [],
   "source": [
    "def max_cont_sum(arr1):\n",
    "    if len(arr1) == 0:\n",
    "        return 0\n",
    "    \n",
    "    max_sum = current_sum = arr1[0]\n",
    "    \n",
    "    for num in arr1[1:]:\n",
    "        \n",
    "        current_sum = max(current_sum+num,num)\n",
    "        max_sum = max(max_sum,current_sum)\n",
    "        \n",
    "    return max_sum"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 5,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "29"
      ]
     },
     "execution_count": 5,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "arr1 = [1,2,-1,3,4,10,10,-10,-1]\n",
    "max_cont_sum(arr1)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": []
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3",
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
   "version": "3.7.0"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 2
}
