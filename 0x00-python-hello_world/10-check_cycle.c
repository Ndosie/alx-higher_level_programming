#include "lists.h"

/**
 * check_cycle - checks if the list has a cycle
 * @list: linked list
 *
 * Return: 1 if it has cycle or 0 if it does not have
 */
int check_cycle(listint_t *list)
{
	listint_t *current;
	listint_t *temp;

	current = list;
	while (current->next)
	{
		if (current->next == list)
			return (1);
		
		current = current->next
	}
	return (0)
}
