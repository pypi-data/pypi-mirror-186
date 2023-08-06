# wmul_click_utils
Additional utilities for use with Python's click cli library.

## RequiredIf
A `click.Option` that is used when a given option is required only when a 
specified other option is provided. E.G. A password might be required when a
username is provided.

`required_if` is the name of the other option that, if provided, makes this 
option required.

Example:   
```
@click.option("--email_address", type=str, multiple=True,
              help="The e-mail address to which the report should be sent.")
@click.option("--mail_server", type=str, cls=RequiredIf, 
              required_if="email_address", 
              help="The address of the e-mail SMTP server to use.")
@click.option("--mail_username", type=str, cls=RequiredIf, 
              required_if="email_address", 
              help="The username to authenticate with the e-mail server.")
@click.option("--mail_password", type=str, cls=RequiredIf, 
              required_if="email_address",
              help="The password to authenticate with the e-mail server.")
```

## RequiredUnless
Another `click.Option`. Allows an option to be designated as required only if 
some other option is not provided. E.G. An e-mail address and a username. 
Either or both might be provided, but at least one is needed.

`required_unless` is one or more other options in a list. If none of the 
options are present, an error is raised.

Example:   
```
@click.option("--username", type=str cls=RequiredUnless, 
              required_unless=["email_address"])
@click.option("--email_address", type=str, cls=RequiredUnless, 
              required_unless=["username"])
```

## MXWith
Another `click.Option`. Allows two or more options to be designated as mutually 
exclusive. E.G. logging to a logfile or logging to syslog.

`mx_with` is one or more other options in a list that are mutually exclusive 
with this one.

Example:
```
@click.option('--syslog', is_flag=True, cls=MXWith, mx_with=['log_file_name'],
              help="log to syslog.")
@click.option(
    '--log_file_name',
    type=click.Path(
        file_okay=True, 
        dir_okay=False, 
        readable=True,
        writable=True
    ), 
    cls=MXWith,
    mx_with=["syslog"],  
    help="Log to this filename."
)
```

## RequiredUnless / MXWith Comparison
These two operate similarly. The difference is when multiple options or no 
options are provided. 

`RequiredUnless` makes certain that at __least__ one of the options is present. 
Multiple or all of the options may be provided without error. 

`MXWith` makes certain that at __most__ one option is present. If none of the
options are provided, no error is raised.

## PairedParamType / PAIRED
A click.ParamType that allows a parameter to accept a list of pairs. 
The list is in the form of a space-delimited string. E.G. '.wav .mp3' or 
'.wav .mp3 .doc .docx'.

Example
```
@click.option('--equivalent', type=PAIRED,
              help="Pairs of equivalent extensions.")

--equivalent ".wav .mp3 .doc .docx"
```

## DateParamType / DATE
A click.ParamType that allows a parameter to accept a date in the format 
YYYY-MM-DD. 

Example
```
@click.option("--cutoff_date", type=DATE)

--cutoff_date 2023-01-17
```
