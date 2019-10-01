using System.Collections;
using System.Collections.Generic;
using UnityEngine;
using UnityEngine.EventSystems;

public class ControlScript : MonoBehaviour, IBeginDragHandler, IDragHandler
{

    public GameObject square;
    SpriteRenderer spriteSquare;

    public void OnBeginDrag(PointerEventData eventData)
    {
       if ((Mathf.Abs(eventData.delta.x)) > (Mathf.Abs(eventData.delta.y)))
        {
            if (eventData.delta.x > 0)
                spriteSquare.color = Color.blue;
            else
                spriteSquare.color = Color.gray;
        }
       else
        {
            if (eventData.delta.y > 0)
                spriteSquare.color = Color.green;
            else
                spriteSquare.color = Color.yellow;
        }
    }

    public void OnDrag(PointerEventData eventData)
    {
       
    }

    void Start()
    {
        spriteSquare = square.GetComponent<SpriteRenderer>();

    }

   
    void Update()
    {
      
    }
}
