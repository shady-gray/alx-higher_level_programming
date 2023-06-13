#include <stdlib.h>
#include <stdio.h>
#include "lists.h"

/**
  * count_list - will count the number of element in a linked list
  * @m: The linked list to count
  *
  * Return: No of linked list (on Success)
  */
size_t count_list(const listint_t *m)
{
	int len = 0;

	while (m != NULL)
	{
		++len;
		m = m->next;
	}

	return (len);
}

/**
  * get_nodeint_at_index - Gets a node from a linked list
  * @head: The head of the linked list
  * @index: The index to find in the linked list
  *
  * Return: The specific node of the linked list
  */
listint_t *get_nodeint_at_index(listint_t *head, unsigned int index)
{
	listint_t *current = head;
	unsigned int iter_times = 0;

	if (head)
	{
		while (current != NULL)
		{
			if (iter_times == index)
				return (current);

			current = current->next;
			++iter_times;
		}
	}

	return (NULL);
}

/**
  * is_palindrome - Checks if a singly linked list is a palindrome
  * @head: The head of the singly linked list
  *
  * Return: 0 if it is not a palindrome, 1 if it is a palindrome
  */
int is_palindrome(listint_t **head)
{
    listint_t *open = NULL, *close = NULL;
    unsigned int m = 0, len = 0, len_cyc = 0, len_list = 0;

    if (head == NULL)
        return (0);

    if (*head == NULL)
        return (1);
    
    open = *head;
    len = count_list(open);
    len_cyc = len * 2;
    len_list = len_cyc - 2;
    close = *head;

    for (; m < len_cyc; m = m + 2)
    {
        if (open[m].n != close[len_list].n)
            return (0);

        len_list = len_list - 2;
    }

    return (1);
}
