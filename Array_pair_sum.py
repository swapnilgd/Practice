{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 27,
   "metadata": {},
   "outputs": [],
   "source": [
    "#Array_pair sum ((1,3,2,2)4)\n",
    "#result((1,3)(2,2))\n",
    "\n",
    "def pair_sum(num_list,out):\n",
    "    seen =  set()\n",
    "    output = set()\n",
    "    for nums in num_list:\n",
    "        temp = out - nums\n",
    "        if temp not in seen:\n",
    "            seen.add(nums)\n",
    "        else:\n",
    "            output.add((min(nums,temp),max(nums,temp)))\n",
    "    print(output)\n",
    "    "
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 28,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "{(1, 3), (2, 2)}\n"
     ]
    }
   ],
   "source": [
    "pair_sum((1,3,2,2),4)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 29,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "{(3, 5), (2, 6), (0, 8), (1, 7)}\n"
     ]
    }
   ],
   "source": [
    "pair_sum((2,3,6,4,7,3,1,5,8,0),8)"
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
