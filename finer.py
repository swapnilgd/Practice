{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 27,
   "metadata": {},
   "outputs": [],
   "source": [
    "def finder(arr1,arr2):\n",
    "    \n",
    "    output = {}\n",
    "    \n",
    "    for num1 in arr1:\n",
    "        if num1 in output:\n",
    "            output[num1] += 1\n",
    "        else:\n",
    "            output[num1] = 1\n",
    "    for num2 in arr2:\n",
    "        if num2 in output:\n",
    "            output[num2] -= 1\n",
    "        else:\n",
    "            output[num2] = 1\n",
    " \n",
    "    for k in output:\n",
    "        if output[k] != 0:\n",
    "            print(k)\n",
    "\n",
    "            "
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 36,
   "metadata": {},
   "outputs": [
    {
     "ename": "SyntaxError",
     "evalue": "invalid syntax (<ipython-input-36-4458512d9096>, line 2)",
     "output_type": "error",
     "traceback": [
      "\u001b[0;36m  File \u001b[0;32m\"<ipython-input-36-4458512d9096>\"\u001b[0;36m, line \u001b[0;32m2\u001b[0m\n\u001b[0;31m    arr2 = [6,3,4,5, ,1,7]\u001b[0m\n\u001b[0m                     ^\u001b[0m\n\u001b[0;31mSyntaxError\u001b[0m\u001b[0;31m:\u001b[0m invalid syntax\n"
     ]
    }
   ],
   "source": [
    "arr1 = [1,2,3,4,5,6,7]\n",
    "arr2 = [6,3,4,5, ,1,7]\n",
    "finder(arr1,arr2)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": []
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
