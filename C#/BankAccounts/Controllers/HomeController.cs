using System;
using System.Collections.Generic;
using System.Diagnostics;
using System.Linq;
using System.Threading.Tasks;
using Microsoft.AspNetCore.Mvc;
using System.Data;
using MySql.Data.MySqlClient;
using Microsoft.ApplicationInsights.Extensibility.Implementation;
using BankAccounts.Models;
using Microsoft.EntityFrameworkCore;
using Microsoft.AspNetCore.Http;
using Microsoft.AspNetCore.Identity;

public class HomeController : Controller
{
    private BankContext _context;

    public HomeController (BankContext context)
    {
        _context = context;
    }
 
        [HttpGet]
        [Route("")]
        public IActionResult Index()
        {
            return View();
        }

        [HttpGet]
        [Route("login")]
        public IActionResult loginpage()
        {
            return View("Login");
        }

        [HttpPost]
        [Route("Login")]
        public IActionResult Login(string loginemail, string loginpw)
        {
            var Hasher = new PasswordHasher<User>();
            User usercheck = _context.Users.SingleOrDefault(user => user.Email == loginemail);
            if (usercheck == null || 0 == Hasher.VerifyHashedPassword(usercheck, usercheck.Password, loginpw))
            {
                ViewBag.Message = "You could not be logged in. Please try again.";
                return View("Login");
            }
            else
            {
                HttpContext.Session.SetInt32("UserId", usercheck.UserId);
                return RedirectToAction("Index", "Bank", new { accountNum = HttpContext.Session.GetInt32("UserId")});
            }
        }

        [HttpPost]
        [Route("Register")]
        public IActionResult UserRegistration(RegisterViewModel adduser)
        {
            if(ModelState.IsValid)
            {
                User UserInDB = _context.Users.SingleOrDefault(user => user.Email == adduser.Email);
                if (UserInDB != null)
                {
                    ViewBag.Message = "This email already exists in the database.";
                    return View("Index", adduser);
                }
                PasswordHasher<User> Hasher = new PasswordHasher<User>();
                User AddUserinDB = new User
                {
                    FirstName = adduser.FirstName,
                    LastName = adduser.LastName,
                    Email = adduser.Email,
                    Password = adduser.Password,
                    CreatedAt = DateTime.Now,
                    UpdatedAt = DateTime.Now
                };
                AddUserinDB.Password = Hasher.HashPassword(AddUserinDB, AddUserinDB.Password);
                _context.Add(AddUserinDB);
                _context.SaveChanges();
                AddUserinDB = _context.Users.SingleOrDefault(user => user.Email == AddUserinDB.Email);
                HttpContext.Session.SetInt32("UserId", AddUserinDB.UserId);
                return RedirectToAction ("Account", "Bank", new { accountNum = HttpContext.Session.GetInt32("UserId")});
            }
            else
            {
                return View("Index", adduser);
            }
        }
        
        [HttpGet]
        [Route("Success")]
        public IActionResult Success() 
        {
            return View("Success");
        }

        [HttpGet]
        [Route("Logout")]
        public IActionResult Logout()
        {
            HttpContext.Session.Clear();
            return View("Index");
        }
    }
