#include "lists.h"

/**
 * check_cycle - function checks if a singly linked list has a cycle in it.
 * @list: pointer to the beginning of the node
 *
 * Return: 0 if no cycle, 1 if there is a cycle
 */
int check_cycle(listint_t *list)
{
	listint_t *present, *checker;

	if (list == NULL || list->next == NULL)
		return (0);
	present = list;
	checker = present->next;

	while (present != NULL && checker->next != NULL
		&& checker->next->next != NULL)
	{
		if (present == checker)
			return (1);
		present = present->next;
		checker = checker->next->next;
	}
	return (0);
}

