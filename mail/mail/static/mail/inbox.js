document.addEventListener('DOMContentLoaded', function() {

  // Use buttons to toggle between views
  document.querySelector('#inbox').addEventListener('click', () => load_mailbox('inbox'));
  document.querySelector('#sent').addEventListener('click', () => load_mailbox('sent'));
  document.querySelector('#archived').addEventListener('click', () => load_mailbox('archive'));
  document.querySelector('#compose').addEventListener('click', () => {
    compose_email()
  });
  document.querySelector('#submit-email').addEventListener('click', () => {
    console.log("clicked");
    fetch('/emails', {
      method: 'POST',
      body: JSON.stringify({
        recipients: document.querySelector("#compose-recipients").value,
        subject: document.querySelector("#compose-subject").value,
        body: document.querySelector("#compose-body").value
      })
    })
    .then(response => response.json())
    .then(result => {
      console.log("result: " + result);
    });
    window.location.replace = "/";
  });

  
  // By default, load the inbox
  load_mailbox('inbox');

});




function compose_email(email_data=null) {
  // Show compose view and hide other views
  document.querySelector('#emails-view').style.display = 'none';
  document.querySelector('#compose-view').style.display = 'block';
  document.querySelector('#email-view').style.display = 'none';

  // Clear out composition fields
  if (email_data) {
    console.log(email_data);
    document.querySelector('#compose-recipients').value = email_data.sender;
    if (email_data.subject.slice(0,3) != "Re:") {
      // console.log(email_data.subject.slice(0,3));
      document.querySelector('#compose-subject').value = `Re: ${email_data.subject}`;
    }
    else {
      document.querySelector('#compose-subject').value = email_data.subject;
    }
    document.querySelector('#compose-body').value = `On ${email_data.timestamp}, ${email_data.sender} wrote: ${email_data.body}`;
  }
  else {
    console.log("no email data");
    document.querySelector('#compose-recipients').value = '';
    document.querySelector('#compose-subject').value = '';
    document.querySelector('#compose-body').value = '';
  }
  
}
// display individual email
function load_email(email_id, mailbox) {
  document.querySelector('#emails-view').style.display = 'none';
  document.querySelector('#compose-view').style.display = 'none';
  document.querySelector('#email-view').style.display = 'block';
  const url = `/emails/${email_id}`;
  fetch(url, {
    method: 'PUT',
    body: JSON.stringify({
      read: true
    })
  });
  fetch(url)
    .then(response => response.json())
    .then(email => {
      document.querySelector('#sender').innerHTML = email.sender;
      document.querySelector('#date').innerHTML = email.timestamp;
      document.querySelector('#recipients').innerHTML = email.recipients.toString().replace(/,/g, ', ');
      document.querySelector('#subject').innerHTML = email.subject;
      document.querySelector('#email-content').innerHTML = email.body;
      let archive_btn = document.querySelector('#archive');
      if (mailbox != 'sent'){
        console.log(`mailbox: ${mailbox}`);
        archive_btn.style.display = 'block';
        if (email.archived) {
          archive_btn.innerHTML = "Unarchive";
          archive_btn.addEventListener('click', () => {
            fetch(url, {
              method: 'PUT',
              body: JSON.stringify({
                archived: false
              })
            })
            load_mailbox('inbox');
          })
        }
        else {
          archive_btn.innerHTML = "Archive";
          archive_btn.addEventListener('click', () => {
            fetch(url, {
              method: 'PUT',
              body: JSON.stringify({
                archived: true
              })
            })
            load_mailbox('inbox');
          })
        }
      }
      else {
        archive_btn.style.display = 'none';
      }
      document.querySelector('#reply').addEventListener('click', () => {
        compose_email(email);
      })
    });
}

function load_mailbox(mailbox) {
  
  // Show the mailbox and hide other views
  document.querySelector('#emails-view').style.display = 'block';
  document.querySelector('#compose-view').style.display = 'none';
  document.querySelector('#email-view').style.display = 'none';

  // Show the mailbox name
  document.querySelector('#title').innerHTML = `<h3>${mailbox.charAt(0).toUpperCase() + mailbox.slice(1)}</h3>`;

  // Getting emails
  const url = `/emails/${mailbox}`;
  fetch(url)
  .then(response => response.json())
  .then(emails => {
    let num_emails = emails.length;
    let table = document.getElementById("email-table");
    table.innerHTML = "";
    if (table) {
      console.log("found table")
    }
    else {
      console.log("didn't find table")
    }
    for (let i=0; i<num_emails; i++){
      let row = table.insertRow(i);
      row.setAttribute("class", "email-row");
      row.setAttribute("data-email-id", emails[i].id);
      let name_cell = row.insertCell();
      let subject_cell = row.insertCell();
      let date_cell = row.insertCell();
      if (!emails[i].read){
        name_cell.innerHTML = `<strong>${emails[i].sender}</strong>`;
        subject_cell.innerHTML = `<strong>${emails[i].subject}</strong>`;
        date_cell.innerHTML = `<strong>${emails[i].timestamp}</strong>`;
      }
      else {
        name_cell.innerHTML = `<p>${emails[i].sender}</p>`;
        subject_cell.innerHTML = `<p>${emails[i].subject}</p>`;
        date_cell.innerHTML = `<p>${emails[i].timestamp}</p>`;
      }
      
      let email_tr = document.createElement("tr");
      email_tr.classList.add('email-tr')
      if (!emails[i].read){
        email_tr.innerHTML = `<td><strong>${emails[i].sender}</strong></td>
        <td><strong>${emails[i].subject}</strong></td>
        <td><strong>${emails[i].timestamp}</strong></td>`
      }
      else {
        email_tr.innerHTML = `<td>${emails[i].sender}</td>
        <td>${emails[i].subject}</td>
        <td>${emails[i].timestamp}</td>`
      }
      
    }
  })
  // make emails clickable
  .then( () => {
    const emails_list = document.querySelectorAll(".email-row");
    if (emails_list){
      console.log(`items length: ${emails_list.length}`);
    }
    else{
      console.log("items not selected");
    }
    for (let i = 0; i < emails_list.length; i++) {
      console.log(i);
      emails_list[i].addEventListener('click', () => 
        load_email(emails_list[i].dataset.emailId, mailbox))
  }
  }
  )
 }


