using System.Collections;
using System.Collections.Generic;
using System.Linq;
using UnityEngine;

public class RopeSystem : MonoBehaviour
{
	public DistanceJoint2D ropeJoint;
	public Transform crosshair;
	public SpriteRenderer crosshairSprite;
	public float climbSpeed = 3f;
	public GameObject ropeHingeAnchor;
	public LineRenderer ropeRenderer;
	public LayerMask ropeLayerMask;
	public PlayerMovement playerMovement;
	private bool ropeAttached;
	private Vector2 playerPosition;
	private List<Vector2> ropePositions = new List<Vector2>();
	private bool isColliding;
	private bool distanceSet;
	private Dictionary<Vector2, int> wrapPointsLookup = new Dictionary<Vector2, int>();
	private SpriteRenderer ropeHingeAnchorSprite;
	private float ropeMaxCastDistance = 20f;
	private Rigidbody2D ropeHingeAnchorRb;

	//initialization
	void Awake ()
	{
		ropeJoint.enabled = false;
		playerPosition = transform.position;
		ropeHingeAnchorRb = ropeHingeAnchor.GetComponent<Rigidbody2D>();
		ropeHingeAnchorSprite = ropeHingeAnchor.GetComponent<SpriteRenderer>();
		crosshairSprite.enabled = true;
	}


	private Vector2 GetClosestColliderPointFromRaycastHit(RaycastHit2D hit, PolygonCollider2D polyCollider)
	{
		// turn polygoncollider points from local(default) to world space
		var distanceDictionary = polyCollider.points.ToDictionary<Vector2, float, Vector2>(
			position => Vector2.Distance(hit.point, polyCollider.transform.TransformPoint(position)), 
			position => polyCollider.transform.TransformPoint(position));

		var orderedDictionary = distanceDictionary.OrderBy(e => e.Key);
		return orderedDictionary.Any() ? orderedDictionary.First().Value : Vector2.zero;
	}

	// Update is called once per frame
	void Update ()
	{	//sets aiming position to the mouse position
		var worldMousePosition = Camera.main.ScreenToWorldPoint(new Vector3(Input.mousePosition.x, Input.mousePosition.y, 0f));
		var facingDirection = worldMousePosition - transform.position;
		//calculates angle and stores it
		var aimAngle = Mathf.Atan2(facingDirection.y, facingDirection.x);
		if (aimAngle < 0f)
		{
			aimAngle = Mathf.PI * 2 + aimAngle;
		}
		// calculates and stores the direction
		var aimDirection = Quaternion.Euler(0, 0, aimAngle * Mathf.Rad2Deg) * Vector2.right;
		playerPosition = transform.position;

		if (!ropeAttached)
		{
			SetCrosshairPosition(aimAngle);
			playerMovement.isSwinging = false;
		}
		else
		{
			playerMovement.isSwinging = true;
			playerMovement.ropeHook = ropePositions.Last();
			crosshairSprite.enabled = false;
			//interaction with environment
			if (ropePositions.Count > 0)
			{
				var lastRopePoint = ropePositions.Last();
				var playerToCurrentNextHit = Physics2D.Raycast(playerPosition, (lastRopePoint - playerPosition).normalized, Vector2.Distance(playerPosition, lastRopePoint) - 0.1f, ropeLayerMask);
				if (playerToCurrentNextHit)
				{
					var colliderWithVertices = playerToCurrentNextHit.collider as PolygonCollider2D;
					if (colliderWithVertices != null)
					{
						var closestPointToHit = GetClosestColliderPointFromRaycastHit(playerToCurrentNextHit, colliderWithVertices);
						if (wrapPointsLookup.ContainsKey(closestPointToHit))
						{
							ResetRope();
							return;
						}
						ropePositions.Add(closestPointToHit);
						wrapPointsLookup.Add(closestPointToHit, 0);
						distanceSet = false;
					}
				}
			}
		}
		//must run after every execution
		UpdateRopePositions();
		HandleRopeLength();
		HandleInput(aimDirection);
	}

	private void HandleInput(Vector2 aimDirection)
	{
		if (Input.GetMouseButtonDown (0)) //holding down left click fires grapple and activates sound
			
		{
			Debug.Log ("Working");
			FindObjectOfType<AudioManager> ().Play ("grappleSFX"); 
			if (ropeAttached) return;
			ropeRenderer.enabled = true;

			var hit = Physics2D.Raycast(playerPosition, aimDirection, ropeMaxCastDistance, ropeLayerMask);
			if (hit.collider != null)
			{
				ropeAttached = true;
				if (!ropePositions.Contains(hit.point))
				{
					// Jump slightly to distance the player a little from the ground after grappling to something.
					transform.GetComponent<Rigidbody2D>().AddForce(new Vector2(0f, 2f), ForceMode2D.Impulse);
					ropePositions.Add(hit.point);
					wrapPointsLookup.Add(hit.point, 0);
					ropeJoint.distance = Vector2.Distance(playerPosition, hit.point);
					ropeJoint.enabled = true;
					ropeHingeAnchorSprite.enabled = true;
				}
			}
			else
			{
				ropeRenderer.enabled = false;
				ropeAttached = false;
				ropeJoint.enabled = false;
			}
		}

		if (Input.GetMouseButtonUp (0)) //releases rope and resets grapple
			
		{
			Debug.Log ("working"); 
			ResetRope();
		}
	}
	//complete reset
	private void ResetRope()
	{
		ropeJoint.enabled = false;
		ropeAttached = false;
		playerMovement.isSwinging = false;
		ropeRenderer.positionCount = 2;
		ropeRenderer.SetPosition(0, transform.position);
		ropeRenderer.SetPosition(1, transform.position);
		ropePositions.Clear();
		wrapPointsLookup.Clear();
		ropeHingeAnchorSprite.enabled = false;
	}
		
	//setting crosshair position to mouse position
	private void SetCrosshairPosition(float aimAngle)
	{
		if (!crosshairSprite.enabled)
		{
			crosshairSprite.enabled = true;
		}


		var crossHairPosition = Camera.main.ScreenToWorldPoint(new Vector3(Input.mousePosition.x, Input.mousePosition.y, 10f));
		crosshair.transform.position = crossHairPosition;
	}

	//controls climb up and down 
	private void HandleRopeLength()
	{
		if (Input.GetAxis("Vertical") >= 1f && ropeAttached && !isColliding)
		{
			ropeJoint.distance -= Time.deltaTime * climbSpeed;
		}
		else if (Input.GetAxis("Vertical") < 0f && ropeAttached)
		{
			ropeJoint.distance += Time.deltaTime * climbSpeed;
		}
	}

	//stores rope positions to prevent the player from rubberbanding and the rope from rendering
	private void UpdateRopePositions()
	{
		if (ropeAttached)
		{
			ropeRenderer.positionCount = ropePositions.Count + 1;

			for (var i = ropeRenderer.positionCount - 1; i >= 0; i--)
			{
				if (i != ropeRenderer.positionCount - 1) 
				{
					ropeRenderer.SetPosition(i, ropePositions[i]);


					if (i == ropePositions.Count - 1 || ropePositions.Count == 1)
					{
						if (ropePositions.Count == 1)
						{
							var ropePosition = ropePositions[ropePositions.Count - 1];
							ropeHingeAnchorRb.transform.position = ropePosition;
							if (!distanceSet)
							{
								ropeJoint.distance = Vector2.Distance(transform.position, ropePosition);
								distanceSet = true;
							}
						}
						else 
						{
							var ropePosition = ropePositions[ropePositions.Count - 1];
							ropeHingeAnchorRb.transform.position = ropePosition;
							if (!distanceSet)
							{
								ropeJoint.distance = Vector2.Distance(transform.position, ropePosition);
								distanceSet = true;
							}
						}
					}
					else if (i - 1 == ropePositions.IndexOf(ropePositions.Last()))
					{
						// if the line renderer position we're on is meant for the current anchor/hinge point...
						var ropePosition = ropePositions.Last();
						ropeHingeAnchorRb.transform.position = ropePosition;
						if (!distanceSet)
						{
							ropeJoint.distance = Vector2.Distance(transform.position, ropePosition);
							distanceSet = true;
						}
					}
				}
				else
				{
					// player
					ropeRenderer.SetPosition(i, transform.position);
				}
			}
		}
	}

	void OnTriggerStay2D(Collider2D colliderStay)
	{
		isColliding = true;
	}

	private void OnTriggerExit2D(Collider2D colliderOnExit)
	{
		isColliding = false;
	}
}