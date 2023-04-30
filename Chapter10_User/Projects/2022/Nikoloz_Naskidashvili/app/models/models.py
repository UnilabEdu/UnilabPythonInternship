from app.extensions import db


class BaseModel:
	"""
	SQLAlchemy base model class

	attribs:
		- id: primary key

	methods:
		- Create
		- Read All
		- Update
		- Delete
		- Save
	"""

	id = db.Column(db.Integer, primary_key=True)

	def create(self, commit=None, **kwargs):
		for key, value in kwargs.items():
			setattr(self, key, value)

		if commit is not None:
			self.save()

	@classmethod
	def read_all(cls):
		return cls.query.all()

	def update(self, commit=None, **kwargs):
		for key, value in kwargs.items():
			setattr(self, key, value)

		if commit is not None:
			self.save()

	def delete(self):
		db.session.delete(self)
		db.session.commit()

	def save(self):
		db.session.add(self)
		db.session.commit()

	def __repr__(self):
		return f"<{self.__class__.__name__} model object>"
