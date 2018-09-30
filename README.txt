THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.

FLASK=1.0.2
PYTHON=3.6.6
SQLITE3=3.25.1

pip install the following packages:
	flask
	flask_bootstrap
	flask_sqlalchemy
	werkzeug.security
	flask_login

To configure, set the app config variables in app.py and create_db.py so they point to the same database with the same secret key
To set up tables in the database:
	run python within current directory
	in interpreter, type the following commands:
		>>from create_db import db
		>>db.create_all()
		>>quit()
	
