#include <stdlib.h>
#include "lists.h"
/**
 * insert_node - inserts node into a linked list
 * @head: linked_list
 * number: number to insert
 *
 * Return: address of a new node or NULL if it fails
 */
listint_t *insert_node(listint_t **head, int number)
{
	listint_t *new, *current, *prev_next;
	
	current = *head;
	new = malloc(sizeof(listint_t));
	if (new == NULL)
		return NULL;
	new->n = number;
	new->next = NULL;

	if (*head == NULL)
	{
		*head = new;
		return new;
	}
	else
	{
		while (current-> next)
		{
			if (current->n < number)
			{
				current = current->next;
				prev_next->next = current->next;
			}
			else
			{
				new->next = current;
				prev_next->next = new;
				return new;
			}
		}
	}
	current->next = new;
	return new;
}
