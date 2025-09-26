<h1>WebStore</h1>
<p>A simple Django-based e-commerce web application with REST API support, allowing management of products, users, and orders. Built with Django REST Framework (DRF).</p>

<section>
  <h2>Features</h2>
  <ul>
    <li>User registration and authentication</li>
    <li>Product listing and details</li>
    <li>Widdleware</li>
    <li>REST API endpoints powered by Django REST Framework</li>
    <li>Admin panel to manage products, orders, and users</li>
  </ul>
</section>

<section>
  <h2>Requirements</h2>
  <ul>
    <li>Python 3.9+</li>
    <li>Django 4.x</li>
    <li>djangorestframework</li>
    <li>SQLite (default) or any other database supported by Django</li>
  </ul>
</section>

<section>
  <h2>Installation & Setup</h2>
  <ol>
    <li><strong>Clone the repository:</strong>
      <pre><code>git clone https://github.com/Shrivastava-1/WebStore.git
cd WebStore</code></pre>
    </li>
    <li><strong>Create a virtual environment:</strong>
      <pre><code>python -m venv venv</code></pre>
    </li>
    <li><strong>Activate the virtual environment:</strong>
      <p>Windows:</p>
      <pre><code>venv\Scripts\activate</code></pre>
      <p>Mac/Linux:</p>
      <pre><code>source venv/bin/activate</code></pre>
    </li>
    <li><strong>Install dependencies:</strong>
      <pre><code>pip install -r requirements.txt</code></pre>
      <p>If <code>requirements.txt</code> is not available:</p>
      <pre><code>pip install django
pip install djangorestframework</code></pre>
    </li>
    <li><strong>Apply migrations:</strong>
      <pre><code>python manage.py makemigrations
python manage.py migrate</code></pre>
    </li>
    <li><strong>Create a superuser:</strong>
      <pre><code>python manage.py createsuperuser</code></pre>
    </li>
  </ol>
</section>

<section>
  <h2>Running the Project</h2>
  <pre><code>python manage.py runserver</code></pre>
  <p>Open your browser and visit <a href="http://127.0.0.1:8000/" target="_blank">http://127.0.0.1:8000/</a></p>
  <p>Admin panel: <a href="http://127.0.0.1:8000/admin/" target="_blank">http://127.0.0.1:8000/admin/</a></p>
</section>

<section>
  <h2>API Endpoints</h2>
  <ul>
    <li><code>/api/products/</code> - List and create products</li>
    <li><code>/api/products/&lt;id&gt;/</code> - Retrieve, update, delete a product</li>
    <li><code>/api/orders/</code> - List and create orders</li>
    <li><code>/api/users/</code> - User-related API endpoints</li>
  </ul>
  <p>Replace <code>/api/</code> with your actual API prefix if different.</p>
</section>

<section>
  <h2>Contributing</h2>
  <ol>
    <li>Fork the repository</li>
    <li>Create a feature branch (<code>git checkout -b feature-name</code>)</li>
    <li>Commit your changes (<code>git commit -m "Add feature"</code>)</li>
    <li>Push to the branch (<code>git push origin feature-name</code>)</li>
    <li>Open a Pull Request</li>
  </ol>
</section>

<section>
  <h2>License</h2>
  <p>This project is licensed under the MIT License.</p>
</section>
