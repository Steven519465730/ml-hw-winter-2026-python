{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "99b2aa80",
   "metadata": {},
   "outputs": [],
   "source": [
    "# Ask for input N\n",
    "N = int(input(\"Enter a positive integer (N): \"))\n",
    "\n",
    "# Read N numbers one by one and store them in a list\n",
    "numbers = []\n",
    "for i in range(N):\n",
    "    num = int(input(f\"Enter number {i+1}: \"))\n",
    "    numbers.append(num)\n",
    "\n",
    "# Ask for the search number X\n",
    "X = int(input(\"Enter the number to search for (X): \"))\n",
    "\n",
    "# Search for X in the list\n",
    "if X in numbers:\n",
    "    index = numbers.index(X) + 1  # 1-based index\n",
    "    print(index)\n",
    "else:\n",
    "    print(-1)\n"
   ]
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
   "version": "3.9.13"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}
