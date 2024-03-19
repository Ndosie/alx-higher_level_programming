#include "lists.h"

/**
 * check_cycle - checks if the list has a cycle
 * @list: linked list
 *
 * Return: 1 if it has cycle or 0 if it does not have
 */
int check_cycle(listint_t *list)
{
	listint_t *slow, *fast;

	slow = list;
	fast = list;
	while (fast && fast->next)
	{
		slow = slow->next;
		fast = fast->next->next;
		if (slow == fast)
			return (1);
	}
	return (0);
}
