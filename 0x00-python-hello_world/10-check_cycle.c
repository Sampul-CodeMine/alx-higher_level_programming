#include "lists.h"

/**
 * check_cycle - checks if a linked-list contains a cycle or not
 * @list: linked list to check for cycle
 * Return: 0 if no cycle else 1 if ther is a cycle
*/

int check_cycle(listint_t *list)
{
	listint_t *tender = list;
	listint_t *quick = list;

	if (!list)
		return (0);
	while (tender && quick && quick->next)
	{
		tender = tender->next;
		quick = quick->next->next;
		if (tender == quick)
			return (1);
	}
	return (0);
}
