
using UnityEngine;

public class PlayerMovement : MonoBehaviour
{
	public float jumpSpeed = 10f;
	public Vector2 ropeHook;
	public bool isSwinging;
	public bool groundCheck;
	public float speed = 10f;
	private float jumpInput;
	private float horizontalInput;
	public float swingForce = 4f;
	private Rigidbody2D rBody;
	private bool isJumping;
	private Animator animator;
	private SpriteRenderer playerSprite;


	void Awake()
	{
		//initialize
		playerSprite = GetComponent<SpriteRenderer>();
		rBody = GetComponent<Rigidbody2D>();
		animator = GetComponent<Animator>();
	}

	void Update()
	{
		//controls and checking the ground
		jumpInput = Input.GetAxis("Jump");
		horizontalInput = Input.GetAxis("Horizontal");
		var halfHeight = transform.GetComponent<SpriteRenderer>().bounds.extents.y;
		groundCheck = Physics2D.Raycast(new Vector2(transform.position.x, transform.position.y - halfHeight - 0.04f), Vector2.down, 0.025f);
	}

	void FixedUpdate()
	{
		if (horizontalInput < 0f || horizontalInput > 0f)
		{
			animator.SetFloat("Speed", Mathf.Abs(horizontalInput));
			playerSprite.flipX = horizontalInput < 0f;
			if (isSwinging)
			{
				animator.SetBool("IsSwinging", true);

				// find direction vector from player to hook
				var playerToHookDirection = (ropeHook - (Vector2) transform.position).normalized;

				// Inversed for perpendicular 
				Vector2 perpendicularDirection;
				if (horizontalInput < 0)
				{
					perpendicularDirection = new Vector2(-playerToHookDirection.y, playerToHookDirection.x);
					var leftPerpPos = (Vector2) transform.position - perpendicularDirection*-2f;
					Debug.DrawLine(transform.position, leftPerpPos, Color.green, 0f);
				}
				else
				{
					perpendicularDirection = new Vector2(playerToHookDirection.y, -playerToHookDirection.x);
					var rightPerpPos = (Vector2) transform.position + perpendicularDirection*2f;
					Debug.DrawLine(transform.position, rightPerpPos, Color.green, 0f);
				}

				var force = perpendicularDirection * swingForce;
				rBody.AddForce(force, ForceMode2D.Force);
			}
			else //not swinging, so check if on the ground
			{
				animator.SetBool("IsSwinging", false);

				if (groundCheck)
				{  //momentum determination 
					var groundForce = speed*2f;
					rBody.AddForce(new Vector2((horizontalInput*groundForce - rBody.velocity.x)*groundForce, 0));
					rBody.velocity = new Vector2(rBody.velocity.x, rBody.velocity.y);
				}
			}
		}
		else 
		{  //stops 
			animator.SetBool("IsSwinging", false);
			animator.SetFloat("Speed", 0f);
		}
		// if not swinging, jump function
		if (!isSwinging)
		{
			if (!groundCheck) return;
			isJumping = jumpInput > 0f;

			if (isJumping)
			{
				rBody.velocity = new Vector2(rBody.velocity.x, jumpSpeed);
			}
		}
	}
}

